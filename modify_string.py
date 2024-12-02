from collections import Counter


def modify_string(s):
    # Đếm tần suất của từng ký tự
    freq = Counter(s)

    # Sắp xếp các ký tự:
    # - Theo tần suất giảm dần
    # - Nếu tần suất bằng nhau, sắp xếp theo thứ tự từ điển
    sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))

    # Trả về chuỗi kết quả
    return ''.join(sorted_chars)


# Ví dụ sử dụng
s1 = "codelearn"
s2 = "helloworld"
print(modify_string(s1))  # Output: "eacdlnor"
print(modify_string(s2))  # Output: "lodehrw"
