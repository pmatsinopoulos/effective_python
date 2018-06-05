def sort_priority(values, group):
    with_high_priority_items = [False]

    def helper(x):
        if x in group:
            with_high_priority_items[0] = True
            return 0, x
        return 1, x
    values.sort(key=helper)
    return with_high_priority_items[0]


values = [1, 5, 3, 4, 8, 0]
group = {2, 3, 8}

with_high_priority_items = sort_priority(values, group)

print values
print with_high_priority_items
