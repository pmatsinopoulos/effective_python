def my_generator():
    for i in range(100):
        yield i

def my_func(*args):
    args_str = ', '.join(str(x) for x in args)
    print(args_str)

it = my_generator()
my_func(*it)

