import logging

from functools import wraps

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
                        f'request body: {res.request.body}, url: {res.request.url}')
            logger.info(f'Response status:{res.status_code}, '
                        f'response body: {res.text}, url: {res.request.url}')
            return res
        return inner
    return wrapper
