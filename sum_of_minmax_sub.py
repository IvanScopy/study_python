from collections import deque


def sum_of_min_max(arr, k):
    n = len(arr)

    # Deques để lưu chỉ số của phần tử min và max trong mảng con kích thước k
    min_deque = deque()  # Để lưu chỉ số của phần tử min
    max_deque = deque()  # Để lưu chỉ số của phần tử max

    total_sum = 0

    for i in range(n):
        # Loại bỏ các phần tử đã ra khỏi cửa sổ kích thước k
        if min_deque and min_deque[0] < i - k + 1:
            min_deque.popleft()
        if max_deque and max_deque[0] < i - k + 1:
            max_deque.popleft()

        # Duy trì deque min: loại bỏ các phần tử lớn hơn arr[i] vì chúng không thể là min trong mảng con sau này
        while min_deque and arr[min_deque[-1]] >= arr[i]:
            min_deque.pop()

        # Duy trì deque max: loại bỏ các phần tử nhỏ hơn arr[i] vì chúng không thể là max trong mảng con sau này
        while max_deque and arr[max_deque[-1]] <= arr[i]:
            max_deque.pop()

        # Thêm chỉ số i vào deque
        min_deque.append(i)
        max_deque.append(i)

        # Khi đã duyệt đủ k phần tử, tính tổng min và max
        if i >= k - 1:
            total_sum += arr[min_deque[0]] + arr[max_deque[0]]

    return total_sum


# Ví dụ sử dụng
arr = [2, 5, -1, 7, -3, -1, -2]
k = 4
print(sum_of_min_max(arr, k))  # Kết quả: 18
