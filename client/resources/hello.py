from flask.views import MethodView

from flask_smorest import Blueprint
from celery.result import allow_join_result

from ..tasks import do

blp = Blueprint('Hello', 'hello')


@blp.route("/")
class Hello(MethodView):
    def get(self):
        # <data> should be money or something like that
        data = 1
        #? why dont I call it directly?
        # now I call it directly
        do(100)
        
        return 'Hello'