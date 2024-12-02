# Hàm tô màu đồ thị bằng thuật toán tham lam cải tiến
def improved_greedy_coloring(graph):
    # Số lượng đỉnh trong đồ thị
    n = len(graph)

    # Mảng màu để lưu màu của các đỉnh, -1 nghĩa là chưa có màu
    colors = [-1] * n

    # Danh sách các đỉnh và số lượng kề của chúng
    degree = [(i, len(graph[i])) for i in range(n)]

    # Sắp xếp các đỉnh theo số lượng đỉnh kề giảm dần
    degree.sort(key=lambda x: x[1], reverse=True)

    # Duyệt từng đỉnh trong đồ thị theo thứ tự đã sắp xếp
    for u, _ in degree:
        # Mảng để theo dõi màu nào đã được sử dụng bởi các đỉnh kề
        used_colors = [False] * n

        # Kiểm tra tất cả các đỉnh kề với đỉnh u
        for v in graph[u]:
            if colors[v] != -1:  # Nếu đỉnh v đã được tô màu, đánh dấu màu của nó
                used_colors[colors[v]] = True

        # Tìm màu đầu tiên chưa được sử dụng
        color = 0
        while used_colors[color]:
            color += 1

        # Gán màu cho đỉnh u
        colors[u] = color

    # Trả lại mảng màu của các đỉnh
    return colors


# Ví dụ về đồ thị
graph = [
    [1, 2],  # Đỉnh 0 kề với đỉnh 1 và 2
    [0, 3],  # Đỉnh 1 kề với đỉnh 0 và 3
    [0, 3],  # Đỉnh 2 kề với đỉnh 0 và 3
    [1, 2]  # Đỉnh 3 kề với đỉnh 1 và 2
]

# Thực thi thuật toán tô màu đồ thị
colors = improved_greedy_coloring(graph)

# In kết quả
print("Màu của các đỉnh: ", colors)
