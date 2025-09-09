def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = merge_sort(mylist)
print("Sorted array:", mysortedlist)
