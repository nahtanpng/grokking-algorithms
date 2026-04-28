def count_items(array):
    if len(array) == 0:
        return 0
    return 1 + count_items(array[1:])


print(count_items([1, 2, 3, 4, 5]))
