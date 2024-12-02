def merge(arr1, arr2):
    # Hàm trộn hai mảng đã sắp xếp vào một mảng
    merged = []
    i = j = 0

    # Trộn hai mảng theo thứ tự tăng dần
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Thêm phần còn lại của mảng arr1 nếu có
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Thêm phần còn lại của mảng arr2 nếu có
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def natural_merge(arr):
    # Tìm các Run tự nhiên
    runs = []
    start = 0
    while start < len(arr):
        end = start + 1
        # Tìm một Run tự nhiên (mảng đã sắp xếp)
        while end < len(arr) and arr[end] >= arr[end - 1]:
            end += 1
        # Thêm Run vào danh sách các Runs
        runs.append(arr[start:end])
        start = end

    # Trộn các Run lại với nhau
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                new_runs.append(merge(runs[i], runs[i + 1]))  # Trộn từng đôi Run
            else:
                new_runs.append(runs[i])  # Nếu không có đôi để trộn, thêm Run còn lại
        runs = new_runs  # Cập nhật lại danh sách Runs

    return runs[0]  # Trả về mảng đã được sắp xếp

# Ví dụ
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = natural_merge(arr)
print("Sắp xếp Natural Merge Sort:", sorted_arr)
