import functools
import datetime

def log_calls(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            time = datetime.datetime.now()
            with open(filename, "a") as f:
                f.write(f"{time}: {func.__name__} {args}\n")
            return func(*args)
        return wrapper
    return decorator

@log_calls("calls.log")
def sum(a, b):
    return a + b

sum(2, 3)