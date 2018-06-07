def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100.0 * value / total
        result.append(percent)
    return result


print(normalize([1, 2, 3]))


def read_visits(path):
    with open(path, 'r') as f:
        for line in f:
            yield int(line)


# for line in read_visits('test-data/texas-visits.txt'):
#     print(line)


def normalize_copy(numbers):
    list_of_numbers = list(numbers)
    total = sum(list_of_numbers)
    result = []
    for num in list_of_numbers:
        percent = 100.0 * num / total
        result.append(percent)
    return result


print(normalize_copy(read_visits('test-data/texas-visits.txt')))


def normalize_func(get_iterator):
    total = sum(get_iterator())
    result = []
    for num in get_iterator():
        percent = 100.0 * num / total
        result.append(percent)

    return result


print(normalize_func(lambda: read_visits('test-data/texas-visits.txt')))


class ReadVisits():
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits('test-data/texas-visits.txt')
print(normalize(visits))


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100.0 * value / total
        result.append(percent)
    return result


visits = ReadVisits('test-data/texas-visits.txt')
print(normalize(list(visits)))

print(normalize(iter(visits)))
