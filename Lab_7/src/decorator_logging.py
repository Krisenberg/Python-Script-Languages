import logging
import inspect
import time
import types

def log(level):
    log_format = '%(asctime)s - %(levelname)s: %(message)s'
    logging.basicConfig(level=level, format=log_format)
    logger = logging.getLogger()
    
    def log_decorator(object):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = object(*args, **kwargs)
            end = time.perf_counter()
            exec_time = end - start
            info = ''
            if inspect.isclass(object):
                info = (f"Creation time: {start}; Class name: {object.__name__};" +
                        f"Constructor's args: {args}, kwargs: {kwargs}")
            elif isinstance(object, types.FunctionType):
                info = (f"Call time: {start}; Exec duration: {exec_time}" +
                        f"Function name: {object.__name__}; Function's args: {args}, kwargs: {kwargs}" +
                        f"Function's result: {result}")
            logger.log(level,info)
            return result
        return wrapper
    return log_decorator
        