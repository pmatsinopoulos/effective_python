def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            print('...ignoring overflow')
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


print(safe_division(number=1, divisor=10**5000, ignore_overflow=True, ignore_zero_division=False))
print(safe_division(1, 0, True, True))

"""In Python 3:
We can force the use of keyword arguments for the caller:

def safe_division(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):

The above makes the "ignore_overflow" and "ignore_zero_division" to be keyword only arguments.
"""