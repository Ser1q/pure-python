def quicksort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence

    pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


quicksort([1, 2, 7, 5, 2, 0, 6, 4, 2, 2, 8, 4, 10])
