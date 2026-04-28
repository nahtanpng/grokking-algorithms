def find_high_value(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return max(array[0], find_high_value(array[1:]))


print(find_high_value([1, 2, 3, 4, 5]))
