from collections import Counter


def count_characters(s):
    # Đếm tần suất xuất hiện của các ký tự trong chuỗi
    freq = Counter(s)

    # Sắp xếp các ký tự theo thứ tự từ điển
    sorted_chars = sorted(freq.items())

    # Tạo danh sách kết quả
    result = [f"{char} {count}" for char, count in sorted_chars]

    return result


# Ví dụ sử dụng
s1 = "aacccd"
s2 = "aabbbca"
print(count_characters(s1))  # Output: ['a 2', 'c 3', 'd 1']
print(count_characters(s2))  # Output: ['a 3', 'b 3', 'c 1']
