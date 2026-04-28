def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # first call: 10
        # second call: 5
        # third call: 2
        less = [i for i in array[1:] if i <= pivot]
        # first call: 5,2,3
        # second call: 2,3
        # third call: []
        greater = [i for i in array[1:] if i > pivot]
        # first call: []
        # second call: []
        # third call: 3
        return quicksort(less) + [pivot] + quicksort(greater)
        # first call: quicksort([5, 2, 3]) + [10] + quicksort([])
        # second call: quicksort([2, 3]) + [5] + quicksort([])
        # third call: quicksort([]) + [2] + quicksort([3])
        # first return: [] + [2] + [3]
        # second return: [2,3] + [5] + []
        # third return: [2,3,5] + [10] + []


print(quicksort([10, 5, 2, 3]))
