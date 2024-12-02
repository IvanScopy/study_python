from collections import Counter


def count_frequencies(arr):
    # Đếm tần suất xuất hiện của từng phần tử
    freq = Counter(arr)

    # Sắp xếp các phần tử theo thứ tự tăng dần và in tần suất
    for key in sorted(freq):
        print(f"{key}: {freq[key]}")


# Ví dụ sử dụng
arr = [4, 3, 2, 1, 2, 3, 3, 4, 4, 4, 5]
count_frequencies(arr)
