import inspect


def alias(*names):
    def decorator(func):
        glob = inspect.stack()[1][0].f_globals
        for name in names:
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            wrapper.__name__ = name
            wrapper.__doc__ = func.__doc__
            glob[name] = wrapper
        return func
    return decorator
