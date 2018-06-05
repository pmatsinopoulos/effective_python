def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


print(divide(6, 3)[1])
print(divide(6, 0)[0])
