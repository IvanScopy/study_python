import heapq


def prim_mst(graph, start=0):
    # Số đỉnh của đồ thị
    num_vertices = len(graph)

    # Đánh dấu các đỉnh đã được thêm vào MST
    visited = [False] * num_vertices

    # Hàng đợi ưu tiên cho các cạnh với trọng số nhỏ nhất
    min_heap = []

    # Thêm tất cả cạnh từ đỉnh start vào hàng đợi ưu tiên
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    # Đánh dấu đỉnh bắt đầu là đã thăm
    visited[start] = True
    mst_edges = []
    total_weight = 0

    while min_heap:
        # Chọn cạnh có trọng số nhỏ nhất
        weight, u, v = heapq.heappop(min_heap)

        # Nếu đỉnh v chưa nằm trong MST
        if not visited[v]:
            visited[v] = True
            mst_edges.append((u, v, weight))
            total_weight += weight

            # Thêm tất cả cạnh từ đỉnh v vào hàng đợi nếu đỉnh đó chưa được thăm
            for neighbor, edge_weight in graph[v]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return mst_edges, total_weight


# Ví dụ đồ thị dưới dạng danh sách kề
# Đồ thị không có hướng
# Mỗi phần tử trong graph là danh sách các cặp (đỉnh kề, trọng số)
graph = [
    [(1, 2), (3, 6)],  # Đỉnh 0
    [(0, 2), (2, 3), (3, 8), (4, 5)],  # Đỉnh 1
    [(1, 3), (4, 7)],  # Đỉnh 2
    [(0, 6), (1, 8), (4, 9)],  # Đỉnh 3
    [(1, 5), (2, 7), (3, 9)]  # Đỉnh 4
]

# Chạy thuật toán Prim từ đỉnh 0
mst_edges, total_weight = prim_mst(graph, start=0)
print("Các cạnh trong cây bao trùm tối thiểu:")
for u, v, weight in mst_edges:
    print(f"Cạnh {u} - {v} với trọng số {weight}")
print("Tổng trọng số của cây bao trùm tối thiểu:", total_weight)
