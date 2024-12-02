from collections import Counter


def most_frequent_elements(arr):
    # Đếm tần suất các phần tử
    freq = Counter(arr)

    # Tìm tần suất lớn nhất
    max_freq = max(freq.values())

    # Lọc và in các phần tử có tần suất lớn nhất
    result = [key for key, value in freq.items() if value == max_freq]

    return result


# Ví dụ sử dụng
arr = [4, 7, 2, 8, 4, 8, 3, 2]
result = most_frequent_elements(arr)
print(result)  # Output: [2, 4, 8]
