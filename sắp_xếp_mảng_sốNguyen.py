def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def custom_sorf(a,b):
    sum_a= sum_of_digits(a)
    sum_b= sum_of_digits(b)

    if sum_a != sum_b:
        return sum_a - sum_b  # So sánh theo tổng chữ số
    else:
        return a - b  # Nếu tổng chữ số bằng nhau, so sánh theo giá trị số

# Mảng ví dụ
arr = [13, 20, 7, 4]

# Sắp xếp mảng theo quy tắc đã mô tả
sorted_arr = sorted(arr, key=lambda x: (sum_of_digits(x), x))

print(sorted_arr)