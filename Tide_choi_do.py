from collections import deque

def find_first_element_at_nth_move(N):
    # Khởi tạo queue ban đầu với 5 số 1, 2, 3, 4, 5
    queue = deque([1, 2, 3, 4, 5])

    # Tiến hành các lượt chơi
    for _ in range(N):
        # Xóa phần tử đầu tiên khỏi queue
        first = queue.popleft()
        # Thêm phần tử đó vào cuối queue hai lần
        queue.append(first)
        queue.append(first)

    # Trả về phần tử đầu tiên của queue sau N lượt
    return queue[0]

# Ví dụ sử dụng
N = int(input("Nhập vào số lượt chơi N: "))
result = find_first_element_at_nth_move(N)
print(f"Số đầu tiên của queue tại lượt chơi thứ {N} là: {result}")
