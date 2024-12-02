from collections import deque

def max_in_subarrays(arr, k):
    n = len(arr)
    dq = deque()  # Deque để lưu chỉ số của các phần tử
    result = []

    for i in range(n):
        # Loại bỏ các phần tử đã ra khỏi cửa sổ kích thước k
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Loại bỏ các phần tử nhỏ hơn arr[i] vì chúng sẽ không còn được chọn
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Thêm phần tử hiện tại vào deque
        dq.append(i)

        # Khi đã duyệt đủ k phần tử, thêm phần tử lớn nhất (ở đầu deque) vào kết quả
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Ví dụ sử dụng:
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 2
print(max_in_subarrays(arr, k))
