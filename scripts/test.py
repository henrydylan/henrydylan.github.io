
def add_method(cls):
    def decorator(fn):
        setattr(cls, fn.__name__, fn)
        return fn
    return decorator


class A:
    pass


@add_method(A)
def f(self, x):
    return x**2

