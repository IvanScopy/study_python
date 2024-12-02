import heapq


def trapRainWater(heightMap):
    if not heightMap or not heightMap[0]:
        return 0

    M, N = len(heightMap), len(heightMap[0])
    visited = [[False] * N for _ in range(M)]

    # Min-heap để lấy các ô có độ cao thấp nhất
    heap = []

    # Thêm tất cả các ô biên vào heap và đánh dấu là đã thăm
    for i in range(M):
        for j in range(N):
            if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

    # Các hướng đi: lên, xuống, trái, phải
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    water = 0

    # Duyệt qua các ô trong heap
    while heap:
        height, x, y = heapq.heappop(heap)

        # Kiểm tra các điểm xung quanh
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Nếu điểm (nx, ny) hợp lệ và chưa được thăm
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                # Nếu độ cao của ô kề nhỏ hơn độ cao của ô hiện tại, nước có thể đọng lại
                if heightMap[nx][ny] < height:
                    water += height - heightMap[nx][ny]
                # Đưa độ cao mới vào heap
                heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))

    return water


# Hàm kiểm tra ví dụ
def main():
    heightMap = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]

    result = trapRainWater(heightMap)
    print("Tổng thể tích nước đọng lại:", result)


# Chạy chương trình
main()
