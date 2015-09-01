def twist(twister):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print twister
            return function(*args, **kwargs)
        return wrapper
    return decorator

@twist('hi there')
def add(x,y): return x + y