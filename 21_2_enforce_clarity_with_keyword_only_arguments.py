def print_args(*args, **kwargs):
    """

    :param args: Variable number of position arguments
    :param kwargs: Variable number of keyword arguments
    :return:
    """

    print("Positional: {}".format(args))
    print("Keyword: {}".format(kwargs))


print_args(1, 2, 3, foo='bar', cool='sleep')


def safe_division(number, divisor, **kwargs):
    ignore_zero_division_error = kwargs.pop('ignore_zero_division_error', False)
    if kwargs:
        raise TypeError('too many keyword arguments')

    try:
        return number / divisor
    except ZeroDivisionError:
        if ignore_zero_division_error:
            return float('inf')
        else:
            raise


print(safe_division(5, 3))
print(safe_division(5, 0, ignore_zero_division_error=True))
print(safe_division(5, 0, ignore_zero_division_error=True, foo='bar'))

