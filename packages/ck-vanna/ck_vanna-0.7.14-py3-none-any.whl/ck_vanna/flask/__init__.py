import json
import logging
import os
import sys
import uuid
from abc import ABC, abstractmethod
from functools import wraps
import importlib.metadata

import flask
import requests
from flasgger import Swagger
from flask import Flask, Response, jsonify, request, send_from_directory
from flask_sock import Sock

from ..base import VannaBase
from .assets import css_content, html_content, js_content
from .auth import AuthInterface, NoAuth


class Cache(ABC):
    """
    Define the interface for a cache that can be used to store data in a Flask app.
    """

    @abstractmethod
    def generate_id(self, *args, **kwargs):
        """
        Generate a unique ID for the cache.
        """
        pass

    @abstractmethod
    def get(self, id, field):
        """
        Get a value from the cache.
        """
        pass

    @abstractmethod
    def get_all(self, field_list) -> list:
        """
        Get all values from the cache.
        """
        pass

    @abstractmethod
    def set(self, id, field, value):
        """
        Set a value in the cache.
        """
        pass

    @abstractmethod
    def delete(self, id):
        """
        Delete a value from the cache.
        """
        pass


class MemoryCache(Cache):
    def __init__(self):
        self.cache = {}

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        if id not in self.cache:
            self.cache[id] = {}

        self.cache[id][field] = value

    def get(self, id, field):
        if id not in self.cache:
            return None

        if field not in self.cache[id]:
            return None

        return self.cache[id][field]

    def get_all(self, field_list) -> list:
        return [
            {"id": id, **{field: self.get(id=id, field=field) for field in field_list}}
            for id in self.cache
        ]

    def delete(self, id):
        if id in self.cache:
            del self.cache[id]


class VannaFlaskAPI:
    flask_app = None

    def requires_cache(self, required_fields, optional_fields=[]):
        def decorator(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                id = request.args.get("id")

                if id is None:
                    id = request.json.get("id")
                    if id is None:
                        return jsonify({"type": "error", "error": "No id provided"})

                for field in required_fields:
                    if self.cache.get(id=id, field=field) is None:
                        return jsonify({"type": "error", "error": f"No {field} found"})

                field_values = {
                    field: self.cache.get(id=id, field=field) for field in required_fields
                }

                for field in optional_fields:
                    field_values[field] = self.cache.get(id=id, field=field)

                # Add the id to the field_values
                field_values["id"] = id

                return f(*args, **field_values, **kwargs)

            return decorated

        return decorator

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = self.auth.get_user(flask.request)

            if not self.auth.is_logged_in(user):
                return jsonify({"type": "not_logged_in", "html": self.auth.login_form()})

            # Pass the user to the function
            return f(*args, user=user, **kwargs)

        return decorated

    def __init__(
        self,
        vn: VannaBase,
        cache: Cache = MemoryCache(),
        auth: AuthInterface = NoAuth(),
        debug=True,
        allow_llm_to_see_data=False,
        chart=True,
    ):
        """
        Expose a Flask API that can be used to interact with a Vanna instance.

        Args:
            vn: The Vanna instance to interact with.
            cache: The cache to use. Defaults to MemoryCache, which uses an in-memory cache. You can also pass in a custom cache that implements the Cache interface.
            auth: The authentication method to use. Defaults to NoAuth, which doesn't require authentication. You can also pass in a custom authentication method that implements the AuthInterface interface.
            debug: Show the debug console. Defaults to True.
            allow_llm_to_see_data: Whether to allow the LLM to see data. Defaults to False.
            chart: Whether to show the chart output in the UI. Defaults to True.

        Returns:
            None
        """

        self.flask_app = Flask(__name__)

        self.swagger = Swagger(
          self.flask_app, template={"info": {"title": "Vanna API"}}
        )
        self.sock = Sock(self.flask_app)
        self.ws_clients = []
        self.vn = vn
        self.auth = auth
        self.cache = cache
        self.debug = debug
        self.allow_llm_to_see_data = allow_llm_to_see_data
        self.chart = chart
        self.config = {
          "debug": debug,
          "allow_llm_to_see_data": allow_llm_to_see_data,
          "chart": chart,
        }
        log = logging.getLogger("werkzeug")
        log.setLevel(logging.ERROR)

        if "google.colab" in sys.modules:
            self.debug = False
            print("Google Colab doesn't support running websocket servers. Disabling debug mode.")

        if self.debug:
            def log(message, title="Info"):
                [ws.send(json.dumps({'message': message, 'title': title})) for ws in self.ws_clients]

            self.vn.log = log

        @self.flask_app.route("/api/v0/get_config", methods=["GET"])
        @self.requires_auth
        def get_config(user: any):
            """
            Get the configuration for a user
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: config
                    config:
                      type: object
            """
            config = self.auth.override_config_for_user(user, self.config)
            return jsonify(
                {
                    "type": "config",
                    "config": config
                }
            )

        @self.flask_app.route("/api/v0/generate_questions", methods=["GET"])
        @self.requires_auth
        def generate_questions(user: any):
            """
            Generate questions
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_list
                    questions:
                      type: array
                      items:
                        type: string
                    header:
                      type: string
                      default: Here are some questions you can ask
            """
            # If self has an _model attribute and model=='chinook'
            if hasattr(self.vn, "_model") and self.vn._model == "chinook":
                return jsonify(
                    {
                        "type": "question_list",
                        "questions": [
                            "What are the top 10 artists by sales?",
                            "What are the total sales per year by country?",
                            "Who is the top selling artist in each genre? Show the sales numbers.",
                            "How do the employees rank in terms of sales performance?",
                            "Which 5 cities have the most customers?",
                        ],
                        "header": "Here are some questions you can ask:",
                    }
                )

            training_data = vn.get_training_data()

            # If training data is None or empty
            if training_data is None or len(training_data) == 0:
                return jsonify(
                    {
                        "type": "error",
                        "error": "No training data found. Please add some training data first.",
                    }
                )

            # Get the questions from the training data
            try:
                # Filter training data to only include questions where the question is not null
                questions = (
                    training_data[training_data["question"].notnull()]
                    .sample(5)["question"]
                    .tolist()
                )

                # Temporarily this will just return an empty list
                return jsonify(
                    {
                        "type": "question_list",
                        "questions": questions,
                        "header": "Here are some questions you can ask",
                    }
                )
            except Exception as e:
                return jsonify(
                    {
                        "type": "question_list",
                        "questions": [],
                        "header": "",
                    }
                )

        @self.flask_app.route("/api/v0/generate_sql", methods=["GET"])
        @self.requires_auth
        def generate_sql(user: any):
            """
            Generate SQL from a question
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: query
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: sql
                    id:
                      type: string
                    text:
                      type: string
            """
            question = flask.request.args.get("question")

            if question is None:
                return jsonify({"type": "error", "error": "No question provided"})

            id = self.cache.generate_id(question=question)
            sql = vn.generate_sql(question=question, allow_llm_to_see_data=self.allow_llm_to_see_data)

            self.cache.set(id=id, field="question", value=question)
            self.cache.set(id=id, field="sql", value=sql)

            if vn.is_sql_valid(sql=sql):
                return jsonify(
                    {
                        "type": "sql",
                        "id": id,
                        "text": sql,
                    }
                )
            else:
                return jsonify(
                    {
                        "type": "text",
                        "id": id,
                        "text": sql,
                    }
                )

        @self.flask_app.route("/api/v0/generate_rewritten_question", methods=["GET"])
        @self.requires_auth
        def generate_rewritten_question(user: any):
            """
            Generate a rewritten question
            ---
            parameters:
              - name: last_question
                in: query
                type: string
                required: true
              - name: new_question
                in: query
                type: string
                required: true
            """

            last_question = flask.request.args.get("last_question")
            new_question = flask.request.args.get("new_question")

            rewritten_question = self.vn.generate_rewritten_question(last_question, new_question)

            return jsonify({"type": "rewritten_question", "question": rewritten_question})

        @self.flask_app.route("/api/v0/get_function", methods=["GET"])
        @self.requires_auth
        def get_function(user: any):
            """
            Get a function from a question
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: query
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: function
                    id:
                      type: object
                    function:
                      type: string
            """
            question = flask.request.args.get("question")

            if question is None:
                return jsonify({"type": "error", "error": "No question provided"})

            if not hasattr(vn, "get_function"):
                return jsonify({"type": "error", "error": "This setup does not support function generation."})

            id = self.cache.generate_id(question=question)
            function = vn.get_function(question=question)

            if function is None:
                return jsonify({"type": "error", "error": "No function found"})

            if 'instantiated_sql' not in function:
                self.vn.log(f"No instantiated SQL found for {question} in {function}")
                return jsonify({"type": "error", "error": "No instantiated SQL found"})

            self.cache.set(id=id, field="question", value=question)
            self.cache.set(id=id, field="sql", value=function['instantiated_sql'])

            if 'instantiated_post_processing_code' in function and function['instantiated_post_processing_code'] is not None and len(function['instantiated_post_processing_code']) > 0:
                self.cache.set(id=id, field="plotly_code", value=function['instantiated_post_processing_code'])

            return jsonify(
                {
                    "type": "function",
                    "id": id,
                    "function": function,
                }
            )

        @self.flask_app.route("/api/v0/get_all_functions", methods=["GET"])
        @self.requires_auth
        def get_all_functions(user: any):
            """
            Get all the functions
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: functions
                    functions:
                      type: array
            """
            if not hasattr(vn, "get_all_functions"):
                return jsonify({"type": "error", "error": "This setup does not support function generation."})

            functions = vn.get_all_functions()

            return jsonify(
                {
                    "type": "functions",
                    "functions": functions,
                }
            )

        @self.flask_app.route("/api/v0/run_sql", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(["sql"])
        def run_sql(user: any, id: str, sql: str):
            """
            Run SQL
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: df
                    id:
                      type: string
                    df:
                      type: object
                    should_generate_chart:
                      type: boolean
            """
            try:
                if not vn.run_sql_is_set:
                    return jsonify(
                        {
                            "type": "error",
                            "error": "Please connect to a database using vn.connect_to_... in order to run SQL queries.",
                        }
                    )

                df = vn.run_sql(sql=sql)

                self.cache.set(id=id, field="df", value=df)

                return jsonify(
                    {
                        "type": "df",
                        "id": id,
                        "df": df.head(10).to_json(orient='records', date_format='iso'),
                        "should_generate_chart": self.chart and vn.should_generate_chart(df),
                    }
                )

            except Exception as e:
                return jsonify({"type": "sql_error", "error": str(e)})

        @self.flask_app.route("/api/v0/fix_sql", methods=["POST"])
        @self.requires_auth
        @self.requires_cache(["question", "sql"])
        def fix_sql(user: any, id: str, question: str, sql: str):
            """
            Fix SQL
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
              - name: error
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: sql
                    id:
                      type: string
                    text:
                      type: string
            """
            error = flask.request.json.get("error")

            if error is None:
                return jsonify({"type": "error", "error": "No error provided"})

            question = f"I have an error: {error}\n\nHere is the SQL I tried to run: {sql}\n\nThis is the question I was trying to answer: {question}\n\nCan you rewrite the SQL to fix the error?"

            fixed_sql = vn.generate_sql(question=question)

            self.cache.set(id=id, field="sql", value=fixed_sql)

            return jsonify(
                {
                    "type": "sql",
                    "id": id,
                    "text": fixed_sql,
                }
            )


        @self.flask_app.route('/api/v0/update_sql', methods=['POST'])
        @self.requires_auth
        @self.requires_cache([])
        def update_sql(user: any, id: str):
            """
            Update SQL
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
              - name: sql
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: sql
                    id:
                      type: string
                    text:
                      type: string
            """
            sql = flask.request.json.get('sql')

            if sql is None:
                return jsonify({"type": "error", "error": "No sql provided"})

            self.cache.set(id=id, field='sql', value=sql)

            return jsonify(
                {
                    "type": "sql",
                    "id": id,
                    "text": sql,
                })

        @self.flask_app.route("/api/v0/download_csv", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(["df"])
        def download_csv(user: any, id: str, df):
            """
            Download CSV
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                description: download CSV
            """
            csv = df.to_csv()

            return Response(
                csv,
                mimetype="text/csv",
                headers={"Content-disposition": f"attachment; filename={id}.csv"},
            )

        @self.flask_app.route("/api/v0/generate_plotly_figure", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(["df", "question", "sql"])
        def generate_plotly_figure(user: any, id: str, df, question, sql):
            """
            Generate plotly figure
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
              - name: chart_instructions
                in: body
                type: string
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: plotly_figure
                    id:
                      type: string
                    fig:
                      type: object
            """
            chart_instructions = flask.request.args.get('chart_instructions')

            try:
                # If chart_instructions is not set then attempt to retrieve the code from the cache
                if chart_instructions is None or len(chart_instructions) == 0:
                    code = self.cache.get(id=id, field="plotly_code")
                else:
                    question = f"{question}. When generating the chart, use these special instructions: {chart_instructions}"
                    code = vn.generate_plotly_code(
                        question=question,
                        sql=sql,
                        df_metadata=f"Running df.dtypes gives:\n {df.dtypes}",
                    )
                    self.cache.set(id=id, field="plotly_code", value=code)

                fig = vn.get_plotly_figure(plotly_code=code, df=df, dark_mode=False)
                fig_json = fig.to_json()

                self.cache.set(id=id, field="fig_json", value=fig_json)

                return jsonify(
                    {
                        "type": "plotly_figure",
                        "id": id,
                        "fig": fig_json,
                    }
                )
            except Exception as e:
                # Print the stack trace
                import traceback

                traceback.print_exc()

                return jsonify({"type": "error", "error": str(e)})

        @self.flask_app.route("/api/v0/get_training_data", methods=["GET"])
        @self.requires_auth
        def get_training_data(user: any):
            """
            Get all training data
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: df
                    id:
                      type: string
                      default: training_data
                    df:
                      type: object
            """
            df = vn.get_training_data()

            if df is None or len(df) == 0:
                return jsonify(
                    {
                        "type": "error",
                        "error": "No training data found. Please add some training data first.",
                    }
                )

            return jsonify(
                {
                    "type": "df",
                    "id": "training_data",
                    "df": df.to_json(orient="records"),
                }
            )

        @self.flask_app.route("/api/v0/remove_training_data", methods=["POST"])
        @self.requires_auth
        def remove_training_data(user: any):
            """
            Remove training data
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
            """
            # Get id from the JSON body
            id = flask.request.json.get("id")

            if id is None:
                return jsonify({"type": "error", "error": "No id provided"})

            if vn.remove_training_data(id=id):
                return jsonify({"success": True})
            else:
                return jsonify(
                    {"type": "error", "error": "Couldn't remove training data"}
                )

        @self.flask_app.route("/api/v0/train", methods=["POST"])
        @self.requires_auth
        def add_training_data(user: any):
            """
            Add training data
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: body
                type: string
              - name: sql
                in: body
                type: string
              - name: ddl
                in: body
                type: string
              - name: documentation
                in: body
                type: string
            responses:
              200:
                schema:
                  type: object
                  properties:
                    id:
                      type: string
            """
            question = flask.request.json.get("question")
            sql = flask.request.json.get("sql")
            ddl = flask.request.json.get("ddl")
            documentation = flask.request.json.get("documentation")

            try:
                id = vn.train(
                    question=question, sql=sql, ddl=ddl, documentation=documentation
                )

                return jsonify({"id": id})
            except Exception as e:
                print("TRAINING ERROR", e)
                return jsonify({"type": "error", "error": str(e)})

        @self.flask_app.route("/api/v0/create_function", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(["question", "sql"])
        def create_function(user: any, id: str, question: str, sql: str):
            """
            Create function
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: function_template
                    id:
                      type: string
                    function_template:
                      type: object
            """
            plotly_code = self.cache.get(id=id, field="plotly_code")

            if plotly_code is None:
                plotly_code = ""

            function_data = self.vn.create_function(question=question, sql=sql, plotly_code=plotly_code)

            return jsonify(
                {
                    "type": "function_template",
                    "id": id,
                    "function_template": function_data,
                }
            )

        @self.flask_app.route("/api/v0/update_function", methods=["POST"])
        @self.requires_auth
        def update_function(user: any):
            """
            Update function
            ---
            parameters:
              - name: user
                in: query
              - name: old_function_name
                in: body
                type: string
                required: true
              - name: updated_function
                in: body
                type: object
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
            """
            old_function_name = flask.request.json.get("old_function_name")
            updated_function = flask.request.json.get("updated_function")

            print("old_function_name", old_function_name)
            print("updated_function", updated_function)

            updated = vn.update_function(old_function_name=old_function_name, updated_function=updated_function)

            return jsonify({"success": updated})

        @self.flask_app.route("/api/v0/delete_function", methods=["POST"])
        @self.requires_auth
        def delete_function(user: any):
            """
            Delete function
            ---
            parameters:
              - name: user
                in: query
              - name: function_name
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
            """
            function_name = flask.request.json.get("function_name")

            return jsonify({"success": vn.delete_function(function_name=function_name)})

        @self.flask_app.route("/api/v0/generate_followup_questions", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(["df", "question", "sql"])
        def generate_followup_questions(user: any, id: str, df, question, sql):
            """
            Generate followup questions
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_list
                    questions:
                      type: array
                      items:
                        type: string
                    header:
                      type: string
            """
            if self.allow_llm_to_see_data:
                followup_questions = vn.generate_followup_questions(
                    question=question, sql=sql, df=df
                )
                if followup_questions is not None and len(followup_questions) > 5:
                    followup_questions = followup_questions[:5]

                self.cache.set(id=id, field="followup_questions", value=followup_questions)

                return jsonify(
                    {
                        "type": "question_list",
                        "id": id,
                        "questions": followup_questions,
                        "header": "Here are some potential followup questions:",
                    }
                )
            else:
                self.cache.set(id=id, field="followup_questions", value=[])
                return jsonify(
                    {
                        "type": "question_list",
                        "id": id,
                        "questions": [],
                        "header": "Followup Questions can be enabled if you set allow_llm_to_see_data=True",
                    }
                )

        @self.flask_app.route("/api/v0/generate_summary", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(["df", "question"])
        def generate_summary(user: any, id: str, df, question):
            """
            Generate summary
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: text
                    id:
                      type: string
                    text:
                      type: string
            """
            if self.allow_llm_to_see_data:
                summary = vn.generate_summary(question=question, df=df)

                self.cache.set(id=id, field="summary", value=summary)

                return jsonify(
                    {
                        "type": "text",
                        "id": id,
                        "text": summary,
                    }
                )
            else:
                return jsonify(
                    {
                        "type": "text",
                        "id": id,
                        "text": "Summarization can be enabled if you set allow_llm_to_see_data=True",
                    }
                )

        @self.flask_app.route("/api/v0/load_question", methods=["GET"])
        @self.requires_auth
        @self.requires_cache(
            ["question", "sql", "df"],
            optional_fields=["summary", "fig_json"]
        )
        def load_question(user: any, id: str, question, sql, df, fig_json, summary):
            """
            Load question
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_cache
                    id:
                      type: string
                    question:
                      type: string
                    sql:
                      type: string
                    df:
                      type: object
                    fig:
                      type: object
                    summary:
                      type: string
            """
            try:
                return jsonify(
                    {
                        "type": "question_cache",
                        "id": id,
                        "question": question,
                        "sql": sql,
                        "df": df.head(10).to_json(orient="records", date_format="iso"),
                        "fig": fig_json,
                        "summary": summary,
                    }
                )

            except Exception as e:
                return jsonify({"type": "error", "error": str(e)})

        @self.flask_app.route("/api/v0/get_question_history", methods=["GET"])
        @self.requires_auth
        def get_question_history(user: any):
            """
            Get question history
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_history
                    questions:
                      type: array
                      items:
                        type: string
            """
            return jsonify(
                {
                    "type": "question_history",
                    "questions": cache.get_all(field_list=["question"]),
                }
            )

        @self.flask_app.route("/api/v0/<path:catch_all>", methods=["GET", "POST"])
        def catch_all(catch_all):
            return jsonify(
                {"type": "error", "error": "The rest of the API is not ported yet."}
            )

        if self.debug:
            @self.sock.route("/api/v0/log")
            def sock_log(ws):
                self.ws_clients.append(ws)

                try:
                    while True:
                        message = ws.receive()  # This example just reads and ignores to keep the socket open
                finally:
                    self.ws_clients.remove(ws)

    def run(self, *args, **kwargs):
        """
        Run the Flask app.

        Args:
            *args: Arguments to pass to Flask's run method.
            **kwargs: Keyword arguments to pass to Flask's run method.

        Returns:
            None
        """
        if args or kwargs:
            self.flask_app.run(*args, **kwargs)

        else:
            try:
                from google.colab import output

                output.serve_kernel_port_as_window(8084)
                from google.colab.output import eval_js

                print("Your app is running at:")
                print(eval_js("google.colab.kernel.proxyPort(8084)"))
            except:
                print("Your app is running at:")
                print("http://localhost:8084")

            self.flask_app.run(host="0.0.0.0", port=8084, debug=self.debug, use_reloader=False)


class VannaFlaskApp(VannaFlaskAPI):
    def __init__(
        self,
        vn: VannaBase,
        cache: Cache = MemoryCache(),
        auth: AuthInterface = NoAuth(),
        debug=True,
        allow_llm_to_see_data=False,
        logo="https://charleskeith.oss-cn-shanghai.aliyuncs.com/logo/enlarged_image.png",
        title="Welcome to CKC.AI",
        subtitle="CKC AI-powered copilot for SQL queries.",
        show_training_data=True,
        suggested_questions=True,
        sql=True,
        table=True,
        csv_download=True,
        chart=True,
        redraw_chart=True,
        auto_fix_sql=True,
        ask_results_correct=True,
        followup_questions=True,
        summarization=True,
        function_generation=True,
        index_html_path=None,
        assets_folder=None,
    ):
        """
        Expose a Flask app that can be used to interact with a Vanna instance.

        Args:
            vn: The Vanna instance to interact with.
            cache: The cache to use. Defaults to MemoryCache, which uses an in-memory cache. You can also pass in a custom cache that implements the Cache interface.
            auth: The authentication method to use. Defaults to NoAuth, which doesn't require authentication. You can also pass in a custom authentication method that implements the AuthInterface interface.
            debug: Show the debug console. Defaults to True.
            allow_llm_to_see_data: Whether to allow the LLM to see data. Defaults to False.
            logo: The logo to display in the UI. Defaults to the Vanna logo.
            title: The title to display in the UI. Defaults to "Welcome to CK.AI".
            subtitle: The subtitle to display in the UI. Defaults to "Your AI-powered copilot for SQL queries.".
            show_training_data: Whether to show the training data in the UI. Defaults to True.
            suggested_questions: Whether to show suggested questions in the UI. Defaults to True.
            sql: Whether to show the SQL input in the UI. Defaults to True.
            table: Whether to show the table output in the UI. Defaults to True.
            csv_download: Whether to allow downloading the table output as a CSV file. Defaults to True.
            chart: Whether to show the chart output in the UI. Defaults to True.
            redraw_chart: Whether to allow redrawing the chart. Defaults to True.
            auto_fix_sql: Whether to allow auto-fixing SQL errors. Defaults to True.
            ask_results_correct: Whether to ask the user if the results are correct. Defaults to True.
            followup_questions: Whether to show followup questions. Defaults to True.
            summarization: Whether to show summarization. Defaults to True.
            index_html_path: Path to the index.html. Defaults to None, which will use the default index.html
            assets_folder: The location where you'd like to serve the static assets from. Defaults to None, which will use hardcoded Python variables.

        Returns:
            None
        """
        super().__init__(vn, cache, auth, debug, allow_llm_to_see_data, chart)

        self.config["logo"] = logo
        self.config["title"] = title
        self.config["subtitle"] = subtitle
        self.config["show_training_data"] = show_training_data
        self.config["suggested_questions"] = suggested_questions
        self.config["sql"] = sql
        self.config["table"] = table
        self.config["csv_download"] = csv_download
        self.config["chart"] = chart
        self.config["redraw_chart"] = redraw_chart
        self.config["auto_fix_sql"] = auto_fix_sql
        self.config["ask_results_correct"] = ask_results_correct
        self.config["followup_questions"] = followup_questions
        self.config["summarization"] = summarization
        self.config["function_generation"] = function_generation and hasattr(vn, "get_function")
        self.config["version"] = importlib.metadata.version('ck_vanna')

        self.index_html_path = index_html_path
        self.assets_folder = assets_folder

        @self.flask_app.route("/auth/login", methods=["POST"])
        def login():
            return self.auth.login_handler(flask.request)

        @self.flask_app.route("/auth/callback", methods=["GET"])
        def callback():
            return self.auth.callback_handler(flask.request)

        @self.flask_app.route("/auth/logout", methods=["GET"])
        def logout():
            return self.auth.logout_handler(flask.request)


        @self.flask_app.route("/assets/<path:filename>")
        def proxy_assets(filename):
            if self.assets_folder:
                return send_from_directory(self.assets_folder, filename)

            if ".css" in filename:
                return Response(css_content, mimetype="text/css")

            if ".js" in filename:
                return Response(js_content, mimetype="text/javascript")

            # Return 404
            return "File not found", 404

        # Proxy the /vanna.svg file to the remote server
        @self.flask_app.route("/vanna.svg")
        def proxy_vanna_svg():
            svg_data = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1024 1024'><path d='M0 5120 l0 -5120 5120 0 5120 0 0 5120 0 5120 -5120 0 -5120 0 0
-5120z m2648 78 c66 -150 124 -281 127 -290 6 -16 1 -18 -37 -18 l-45 0 -31
70 -31 70 -113 0 -113 0 -32 -70 -31 -70 -46 0 c-25 0 -46 2 -46 3 0 2 17 39
38 83 21 43 80 172 132 286 52 114 98 207 101 208 3 0 60 -123 127 -272z
m-1345 235 c36 -15 37 -16 37 -70 l0 -54 -33 25 c-137 105 -330 -10 -315 -188
12 -146 173 -228 301 -153 l47 28 0 -51 c0 -49 -1 -52 -37 -68 -58 -25 -176
-22 -235 7 -130 63 -193 200 -154 334 49 169 224 254 389 190z m3612 4 c28
-13 75 -59 75 -72 0 -6 -14 -19 -30 -29 -31 -18 -31 -17 -51 8 -16 21 -29 26
-63 26 -52 0 -79 -25 -74 -67 3 -24 16 -35 98 -78 111 -60 133 -88 133 -170 0
-201 -277 -239 -341 -48 -12 37 -11 39 40 48 34 6 36 5 43 -23 22 -102 175
-83 175 21 0 39 -36 75 -113 111 -92 43 -119 71 -124 133 -10 116 121 195 232
140z m1025 -2 c83 -43 81 -149 -3 -215 l-27 -22 42 -51 c23 -29 45 -56 50 -62
5 -5 20 5 37 25 l30 35 27 -27 28 -28 -34 -35 -34 -35 47 -60 c26 -33 47 -62
47 -65 0 -3 -21 -5 -47 -5 -42 0 -51 4 -74 32 l-26 31 -34 -26 c-19 -14 -55
-31 -81 -38 -60 -16 -119 0 -164 45 -63 63 -55 153 21 232 l43 45 -24 42 c-40
70 -25 149 34 181 35 20 105 20 142 1z m1206 -115 c-64 -67 -116 -124 -116
-128 0 -4 52 -72 115 -150 63 -79 115 -145 115 -147 0 -3 -24 -5 -53 -5 l-52
0 -94 120 c-52 66 -98 120 -102 120 -5 0 -9 -54 -9 -120 l0 -120 -45 0 -45 0
0 275 0 275 45 0 45 0 0 -106 0 -107 100 106 c101 106 101 106 153 109 29 2
54 2 56 1 2 -1 -49 -57 -113 -123z m-5456 15 l0 -105 115 0 115 0 0 105 0 105
43 0 42 0 -2 -272 -2 -273 -41 -3 -40 -3 0 130 0 131 -115 0 -115 0 0 -130 0
-130 -45 0 -45 0 0 275 0 275 45 0 45 0 0 -105z m1570 83 c109 -56 108 -211
-2 -273 l-36 -20 79 -110 c43 -61 78 -113 79 -117 0 -5 -21 -8 -47 -8 l-48 1
-80 117 -80 117 -3 -117 -3 -118 -44 0 -45 0 0 275 0 275 93 0 c77 0 100 -4
137 -22z m450 -213 l0 -235 80 0 80 0 -3 -37 -2 -38 -118 0 c-64 0 -117 3
-117 8 0 4 0 126 0 272 l0 265 40 0 40 0 0 -235z m710 194 l0 -40 -107 2 -108
2 -3 -67 -3 -66 111 0 110 0 0 -40 0 -40 -110 0 -110 0 0 -90 0 -90 110 0 110
0 0 -40 0 -40 -150 0 -150 0 0 275 0 275 150 0 150 0 0 -41z m3380 0 l0 -40
-107 2 -108 2 -3 -67 -3 -66 111 0 110 0 0 -40 0 -40 -110 0 -111 0 3 -87 3
-88 108 -3 107 -3 0 -39 0 -40 -150 0 -150 0 0 275 0 275 150 0 150 0 0 -41z
m360 -234 l0 -275 -45 0 -45 0 0 275 0 275 45 0 45 0 0 -275z m560 234 l0 -40
-62 2 -63 3 -2 -235 -2 -234 -40 -3 -41 -3 0 235 0 236 -60 0 -60 0 0 40 0 40
165 0 165 0 0 -41z m308 -64 l-3 -105 115 0 115 0 -3 105 -3 105 45 0 46 0 0
-276 0 -275 -42 3 -43 3 -3 128 -3 128 -110 -3 -111 -3 -1 -125 -2 -125 -42
-3 -43 -3 0 275 0 276 46 0 45 0 -3 -105z'/></svg>"
            return flask.Response(svg_data, mimetype='image/svg+xml')
                excluded_headers = [
                    "content-encoding",
                    "content-length",
                    "transfer-encoding",
                    "connection",
                ]
                headers = [
                    (name, value)
                    for (name, value) in response.raw.headers.items()
                    if name.lower() not in excluded_headers
                ]
                return Response(response.content, response.status_code, headers)
            else:
                return "Error fetching file from remote server", response.status_code

        @self.flask_app.route("/", defaults={"path": ""})
        @self.flask_app.route("/<path:path>")
        def hello(path: str):
            if self.index_html_path:
                directory = os.path.dirname(self.index_html_path)
                filename = os.path.basename(self.index_html_path)
                return send_from_directory(directory=directory, path=filename)
            return html_content
