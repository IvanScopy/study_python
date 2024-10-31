from collections import deque


def max_in_subarrays(arr, k):
    # Danh sách kết quả để lưu các giá trị lớn nhất của từng mảng con
    result = []

    # Deque để lưu chỉ số của các phần tử có ích trong cửa sổ hiện tại kích thước k
    dq = deque()

    for i in range(len(arr)):
        # Loại bỏ các phần tử nằm ngoài cửa sổ hiện tại
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại từ deque
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        # Thêm chỉ số của phần tử hiện tại vào deque
        dq.append(i)

        # Phần tử lớn nhất trong cửa sổ kích thước k là tại dq[0]
        # Chỉ bắt đầu thêm vào danh sách kết quả khi có đủ một cửa sổ đầu tiên
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# Ví dụ sử dụng
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print("Giá trị lớn nhất trong mỗi mảng con:", max_in_subarrays(arr, k))
