import time
results = {}

def timing(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        print(f" время выполнения: {end_time - start_time:.6f} c")
        return result
    return wrapper

@timing
def sum(a, b):
    return a + b

sum(2, 3)
sum(2, 3)
