def sum_of_digits(n):
    # Hàm tính tổng các chữ số của số n
    return sum(int(digit) for digit in str(n))

def custom_sort(arr):
    # Hàm sắp xếp mảng theo nguyên tắc đã cho
    return sorted(arr, key=lambda x: (sum_of_digits(x), x))

# Ví dụ
a = [13, 20, 7, 4]
result = custom_sort(a)
print(result)
