import functools
import datetime
results = {}

def cache(func):
    @functools.wraps(func)
    def wrapper(*args):
        key = args
        if key not in results:
            results[key] = func(*args)
            print(f"[cache-write] {func.__name__}{args}")
        else:
            print(f"[cache-hit] {func.__name__}{args}")
        return results[key]
    
    return wrapper
@cache
def sum(a, b):
    return a + b

sum(2, 3)
sum(2, 3)
