def custom_sort(a, K):
    # Hàm tính trọng số đặc biệt
    return (-a % K, a)  # Dùng -a % K để sắp xếp giảm dần theo trọng số đặc biệt, a để sắp xếp tăng dần theo giá trị nếu trùng trọng số

def sort_array_by_weight(A, K):
    # Sắp xếp mảng A theo trọng số đặc biệt giảm dần, nếu trọng số giống nhau thì theo giá trị tăng dần
    return sorted(A, key=lambda x: (-(x % K), x))

# Mảng ví dụ và số K
A = [10, 20, 30, 15, 25]
K = 6

# Sắp xếp mảng A theo trọng số đặc biệt
sorted_A = sort_array_by_weight(A, K)
print(sorted_A)
