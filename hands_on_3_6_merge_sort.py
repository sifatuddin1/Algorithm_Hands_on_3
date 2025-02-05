
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

   
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

   
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

   
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


array = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_array = merge_sort(array)

print("Original Array:", array)
print("Sorted Array:", sorted_array)