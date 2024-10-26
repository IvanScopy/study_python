from collections import deque

def orangesRotting(grid):
    # so hang va so cot cua ma tran
    rows, cols = len(grid), len(grid[0])

    # hang doi de luu tru cac qua cam hong ban dau
    queue = deque()
    fresh_oranges =0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i,j))
            elif grid[i][j] == 1:
                fresh_oranges += 1

    if fresh_oranges == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    time = 0  # Biến lưu thời gian
    # Thực hiện BFS
    while queue:
        # Để đếm thời gian theo từng "lớp" lây lan
        time += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            # Kiểm tra các ô xung quanh (4 hướng)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Nếu ô xung quanh là quả cam tươi, làm hỏng nó
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # Làm hỏng quả cam tươi
                    fresh_oranges -= 1  # Giảm số quả cam tươi
                    queue.append((nx, ny))  # Thêm quả cam mới bị hỏng vào hàng đợi

    # Nếu còn cam tươi chưa bị hỏng, trả về -1
    return time - 1 if fresh_oranges == 0 else -1

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(orangesRotting(grid))