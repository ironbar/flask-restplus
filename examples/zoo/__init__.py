from flask_restplus import Api

from .cat import api as cat_api, register_resources
from .dog import api as dog_api
from .fake_backend import FakeBackend

api = Api(
    title='Zoo API',
    version='1.0',
    description='A simple demo API',
)

backend = FakeBackend()
register_resources(backend)
api.add_namespace(cat_api, path='/')
api.add_namespace(dog_api)
