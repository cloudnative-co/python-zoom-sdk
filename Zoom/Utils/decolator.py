from .schema import Schemas
from jsonschema import validate, ValidationError

def validation(f):
    def wrapper(*args, **kwargs):
        method_name = f.__qualname__
        schema = Schemas[method_name]
        try:
            validate(kwargs, schema)
        except ValidationError as e:
            raise e
        return f(*args, **kwargs)
    return wrapper
