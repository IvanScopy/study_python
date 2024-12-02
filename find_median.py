from sắp_xếp_mảng_sốNguyen import sorted_arr


def counting_sort(arr):
    max_val= max(arr)
    min_val= min(arr)

    count = [0]*(max_val-min_val+1)

    for num in arr:
        count[num-min_val]+=1

        # Bước 4: Xây dựng lại mảng đã sắp xếp từ mảng đếm
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i + min_val] * freq)

    return sorted_arr

def find_median(arr):

    sorted_arr= counting_sort(arr)

    n=len(sorted_arr)

    if n%2==1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

# Mảng ví dụ
arr = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]

# Tính trung vị
median = find_median(arr)
print(f'Trung vị của mảng là: {median}')