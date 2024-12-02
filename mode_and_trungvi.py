def counting_sort(arr):
    # Xác định giá trị tối đa trong mảng để tạo ra mảng đếm
    max_val = max(arr)
    count = [0] * (max_val + 1)  # Tạo mảng đếm
    output = []

    # Đếm số lần xuất hiện của mỗi giá trị trong mảng
    for num in arr:
        count[num] += 1

    # Xây dựng mảng sắp xếp từ mảng đếm
    for i in range(len(count)):
        output.extend([i] * count[i])

    return output, count


def find_mode(arr):
    _, count = counting_sort(arr)
    max_freq = max(count)

    # Lấy tất cả các giá trị có tần suất lớn nhất
    modes = [i for i, freq in enumerate(count) if freq == max_freq]
    return modes


def find_median(arr):
    arr_sorted, _ = counting_sort(arr)
    n = len(arr_sorted)

    # Nếu số phần tử lẻ, trả về phần tử giữa
    if n % 2 != 0:
        return arr_sorted[n // 2]
    # Nếu số phần tử chẵn, trả về trung bình của hai phần tử giữa
    else:
        return (arr_sorted[(n // 2) - 1] + arr_sorted[n // 2]) / 2


# Ví dụ
A = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]

# Tìm mốt
modes = find_mode(A)
print(f"Mốt của mảng A: {modes}")

# Tìm trung vị
median = find_median(A)
print(f"Trung vị của mảng A: {median}")
