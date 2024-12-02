def merge_runs(arr, left, right):
    if left >= right:
        return arr

    mid = (left + right) // 2
    merge_runs(arr, left, mid)
    merge_runs(arr, mid + 1, right)

    # Merge the two sorted parts
    merge(arr, left, mid, right)
    return arr

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left
    while i < n1 and j < n2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def run_merge_sort(arr):
    return merge_runs(arr, 0, len(arr) - 1)

# Ví dụ
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = run_merge_sort(arr)
print("Sắp xếp Run Merge Sort:", sorted_arr)
