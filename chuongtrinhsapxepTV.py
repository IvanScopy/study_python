import locale

# Thiết lập môi trường ngôn ngữ tiếng Việt
locale.setlocale(locale.LC_COLLATE, "vi_VN.UTF-8")

def sap_xep_tieng_viet(danh_sach):
    """
    Hàm sắp xếp danh sách từ tiếng Việt theo thứ tự từ điển.
    """
    return sorted(danh_sach, key=locale.strxfrm)

# Danh sách từ tiếng Việt cần sắp xếp
danh_sach_tu = [
    "cá", "áo", "an", "táo", "bò", "bờ", "anh", "ăn", "cà", "cả", "cân", "cam"
]

# Sắp xếp danh sách
danh_sach_da_sap_xep = sap_xep_tieng_viet(danh_sach_tu)

# In kết quả
print("Danh sách sau khi sắp xếp:")
for tu in danh_sach_da_sap_xep:
    print(tu)
