from flask.views import MethodView
from flask import current_app
from flask_smorest import Blueprint
from celery.result import allow_join_result

blp = Blueprint('Hello', 'hello')


@blp.route("/")
class Hello(MethodView):
    def get(self):
        result = current_app.extensions['celery'].send_task('orchestrator.do', (1,1))
        with allow_join_result():
            print(result.get())
        return 'Hello'