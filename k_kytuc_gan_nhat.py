def nearest_dorms(dorms, k):
    # Tính khoảng cách bình phương từ (0, 0) đến từng ký túc xá
    dorms_with_distance = [(x, y, x ** 2 + y ** 2) for x, y in dorms]

    # Sắp xếp các ký túc xá theo khoảng cách bình phương (tăng dần)
    dorms_with_distance.sort(key=lambda x: x[2])

    # Lấy k ký túc xá gần nhất
    nearest = [(x, y) for x, y, _ in dorms_with_distance[:k]]

    return nearest


# Ví dụ sử dụng
dorms = [(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)]
k = 10
result = nearest_dorms(dorms, k)
print(result)
