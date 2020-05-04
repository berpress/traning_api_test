import json
import logging

from functools import wraps

from schema import SchemaError, Schema

logger = logging.getLogger()


def logging(message):
    """
    Request Logging
    :param message: message for logging
    :return: response
    """
    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            logger.info(message)
            res = function(*args, **kwargs)
            logger.info(f'Method:{res.request.method}, '
                        f'request body: {res.request.body}, '
                        f'url: {res.request.url}')
            logger.info(f'Response status:{res.status_code}, '
                        f'response body: {res.text}, url: {res.request.url}')
            return res
        return inner
    return wrapper


def is_validate(data: dict, schema: Schema) -> bool:
    """
    Validate json schema
    :return: True if validation is successful else False
    """
    try:
        data = json.loads(json.dumps(data, default=lambda o: o.__dict__))
        schema.validate(data)
        return True
    except SchemaError:
        return False
