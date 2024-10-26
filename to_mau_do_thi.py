import sys

# Hàm tìm đỉnh có trọng số nhỏ nhất từ các đỉnh chưa được đưa vào MST
def min_key(key, mst_set, V):
    min_value = sys.maxsize
    min_index = -1

    for v in range(V):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v

    return min_index

# Hàm thực hiện thuật toán Prim
def prim_mst(graph):
    V = len(graph)  # Số đỉnh của đồ thị

    # Mảng để lưu cây bao trùm tối thiểu
    parent = [-1] * V

    # Mảng lưu giá trị trọng số nhỏ nhất của các cạnh
    key = [sys.maxsize] * V

    # Mảng để theo dõi các đỉnh có trong cây bao trùm tối thiểu
    mst_set = [False] * V

    # Đặt trọng số của đỉnh đầu tiên là 0 để nó được chọn đầu tiên
    key[0] = 0

    for _ in range(V):
        # Chọn đỉnh có trọng số nhỏ nhất từ các đỉnh chưa được chọn
        u = min_key(key, mst_set, V)

        # Đưa đỉnh này vào cây bao trùm tối thiểu
        mst_set[u] = True

        # Cập nhật giá trị trọng số của các đỉnh kề chưa được chọn
        for v in range(V):
            # graph[u][v] là trọng số của cạnh từ u đến v
            if graph[u][v] > 0 and not mst_set[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    # In cây bao trùm tối thiểu
    print("Cạnh   Trọng số")
    for i in range(1, V):
        print(f"{parent[i]} - {i}   {graph[i][parent[i]]}")

# Ví dụ đồ thị (Ma trận trọng số)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)
