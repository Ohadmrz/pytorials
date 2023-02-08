class InvalidArgument(Exception):
    def __init__(self):
        super().__init__()


def numeric_in_range(range_min, range_max):
    def wrapper(orig_func):

        def wrapping_func(*args, **kwargs):
            for a in args + tuple(kwargs.values()):
                if type(a) in (int, float) and \
                        a not in range(range_min, range_max):
                    raise InvalidArgument()
            return orig_func(*args, **kwargs)

        return wrapping_func

    return wrapper

def no_params():
    pass

@numeric_in_range(3, 10)
def one_param(t):
    pass


@numeric_in_range(3, 10)
def multi_params(a, b, c, d=4, e='4'):
    pass


if __name__ == '__main__':
    # one_param(20)
    # one_param(5)
    multi_params('t', True, 5, d=11)