from d15.d15_exceptions import InvalidArgument


def single_str_arg(func):

    def wrapper_func(*args, **kwargs):

        if len(args) != 1 or len(kwargs) != 0 or not isinstance(args[0], str):
            raise InvalidArgument()
        return func(*args, **kwargs)

    return wrapper_func

