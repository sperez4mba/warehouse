from flask_restx import Api

api = Api(
    version="1.0",
    title="Warehouse API",
    description="Warehouse API",
    default="API",
    default_label="",
    doc="/apidocs/",
)
