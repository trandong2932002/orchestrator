from flask import Flask
from flask_smorest import Api

from .celery import celery_init_app
from .resources.hello import blp as HelloBluePrint

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="amqp://172.17.0.2",
            result_backend="redis://172.17.0.3",
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)


    app.config['API_TITLE'] = 'My API'
    app.config['API_VERSION'] = 'alpha'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    api.register_blueprint(HelloBluePrint)

    return app
