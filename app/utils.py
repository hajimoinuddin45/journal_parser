import logging
import time
from functools import wraps

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("journal_parser")

def retry(times, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    time.sleep(delay)
            raise Exception(f"Function {func.__name__} failed after {times} retries.")
        return wrapper
    return decorator
