import json


def decode(data, default=None):
    """
    Loads JSON data into a dictionary

    If the default value is None then we return an empty dictionary.

    :param data:
    :param default:
    :return:
    """
    if default is None:
        default = {}

    try:
        return json.loads(data)
    except ValueError:
        return default


result = decode('{"foo": "bar"}')

print(result)

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print(foo)
print(bar)

