def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncated_prime(num):
    """Kiểm tra xem một số có phải là siêu số nguyên tố dạng cắt giảm không."""
    # Kiểm tra từ phải qua trái (cắt chữ số sau cùng)
    str_num = str(num)
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[:-1]
    return True

def truncated_primes_up_to_n(n):
    """Trả về danh sách các siêu số nguyên tố dạng cắt giảm nhỏ hơn hoặc bằng n."""
    truncated_primes = []
    for i in range(2, n + 1):
        if is_truncated_prime(i):
            truncated_primes.append(i)
    return truncated_primes

# Nhập số từ người dùng
n = int(input("Nhập số n: "))
truncated_primes = truncated_primes_up_to_n(n)

# Hiển thị các siêu số nguyên tố dạng cắt giảm
print("Danh sách siêu số nguyên tố dạng cắt giảm nhỏ hơn hoặc bằng", n, "là:")
print(truncated_primes)
