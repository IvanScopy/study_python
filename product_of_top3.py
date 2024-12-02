def find_product_of_top3(arr):
    n = len(arr)
    result = []

    for i in range(n):
        # Chọn ba số lớn nhất trong mảng từ 0 đến i
        max1 = max2 = max3 = -float('inf')  # Khởi tạo ba số lớn nhất ban đầu

        # Duyệt qua đoạn mảng con từ 0 đến i
        for j in range(i + 1):
            if arr[j] > max1:
                max3 = max2
                max2 = max1
                max1 = arr[j]
            elif arr[j] > max2:
                max3 = max2
                max2 = arr[j]
            elif arr[j] > max3:
                max3 = arr[j]

        # Nếu ba số này hợp lệ (tức có đủ ba số lớn), tính tích và lưu vào kết quả
        if max1 != -float('inf') and max2 != -float('inf') and max3 != -float('inf'):
            result.append(max1 * max2 * max3)
        else:
            result.append(0)  # Trường hợp không đủ ba số

    return result


# Ví dụ sử dụng
arr = [1, 2, 3, 4, 5]
index=len(arr)-1
result = find_product_of_top3(arr)
print(result[index])
