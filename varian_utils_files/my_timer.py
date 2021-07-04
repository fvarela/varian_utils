from .my_logging import Logger
logger = Logger().get_logger()

def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        logger.info(f"Starting timing execution of {orig_func.__name__} at {t1}")
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        logger.info('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper