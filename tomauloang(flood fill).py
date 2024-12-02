def floodFill(image, sr, sc, newColor):
    # Lấy màu ban đầu tại điểm xuất phát
    oldColor = image[sr][sc]

    # Nếu màu mới giống màu cũ, không cần thay đổi gì
    if oldColor == newColor:
        return image

    # Hàm DFS để thực hiện tô màu loang
    def dfs(r, c):
        # Kiểm tra nếu chỉ số r, c nằm trong phạm vi mảng
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return

        # Nếu điểm ảnh có màu khác màu ban đầu, không tô màu
        if image[r][c] != oldColor:
            return

        # Thay đổi màu của điểm ảnh hiện tại
        image[r][c] = newColor

        # Tô màu cho các điểm kề theo 4 hướng
        dfs(r + 1, c)  # Đi xuống
        dfs(r - 1, c)  # Đi lên
        dfs(r, c + 1)  # Đi sang phải
        dfs(r, c - 1)  # Đi sang trái

    # Gọi DFS từ điểm ảnh xuất phát (sr, sc)
    dfs(sr, sc)

    return image


# Hàm chính để kiểm tra chương trình
def main():
    # Mảng ảnh ví dụ
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    # Tọa độ xuất phát (sr, sc) và màu mới
    sr, sc = 1, 1
    newColor = 2

    # Gọi hàm floodFill để tô màu loang
    result = floodFill(image, sr, sc, newColor)

    # In ra kết quả
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
