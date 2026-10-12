def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for arg, t in zip(args, types):
                if not isinstance(arg, t):
                    raise TypeError("Ошибка типов")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

add(2,3)