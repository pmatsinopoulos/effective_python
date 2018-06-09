from collections import defaultdict

names = ['peter', 'panos', 'mary', 'john', 'foo', 'matsinopoulos']

names.sort(key=lambda x: len(x))

print(names)

names = ['peter', 'panos', 'mary', 'john', 'foo', 'matsinopoulos']

print(sorted(names))

print(names)


def log_missing():
    print('key added')
    return 0


current = {'green': 12, 'blue': 8}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

result = defaultdict(log_missing, current)
print('Before: ', dict(result))

for key, amount in increments:
    result[key] += amount


print('After: ', dict(result))


def increment_with_report(current, increments):
    added_count = {'count': 0}

    def missing():
        added_count['count'] += 1
        return 0

    result = defaultdict(missing, current)

    for key, amount in increments:
        result[key] += amount

    return result, added_count['count']


print('Increment with report:', increment_with_report(current, increments))


class AddedCounter:
    def __init__(self):
        self._counter = 0

    def missing(self):
        self._counter += 1
        return 0


added_counter = AddedCounter()


result = defaultdict(added_counter.missing, current)

print('Current: ', current)

for key, amount in increments:
    result[key] = amount

print('Next', dict(result))


class BetterAddedCounter:
    def __init__(self):
        self._counter = 0

    def __call__(self):
        self._counter += 1
        return 0

better_added_counter = BetterAddedCounter()

result = defaultdict(better_added_counter, current)
for key, amount in increments:
    result[key] = amount
print('After: ', dict(result))