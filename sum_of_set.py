def sumOfCommon(arr1, arr2):
    # Chuyển cả hai dãy thành set để loại bỏ phần tử trùng lặp
    set1 = set(arr1)
    set2 = set(arr2)

    # Tìm giao của hai set
    common_elements = set1 & set2

    # Tính tổng các phần tử trong giao
    return sum(common_elements)


# Ví dụ sử dụng
arr1 = [6, 7, 5, 4, 6, 8]
arr2 = [2, 5, 7, 5, 3]
print(sumOfCommon(arr1, arr2))  # Output: 12

arr1 = [5, 6, 7]
arr2 = [2, 3, 4]
print(sumOfCommon(arr1, arr2))  # Output: 0
