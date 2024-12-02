import locale

# Thiết lập locale cho tiếng Việt
locale.setlocale(locale.LC_COLLATE, 'vi_VN.UTF-8')

# Hàm sắp xếp danh sách tiếng Việt
def sort_vietnamese(words):
    # Sắp xếp theo chuẩn tiếng Việt
    return sorted(words, key=locale.strxfrm)

# Ví dụ sử dụng
words = ["học", "học", "tú", "tinh", "tình", "ăn", "zebra", "bạn", "bảo"]
sorted_words = sort_vietnamese(words)
print(sorted_words)
