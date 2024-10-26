def can_complete_circuit(gas, distance):
    n = len(gas)

    total_gas = 0  # Tổng lượng xăng tích lũy (gas - distance) cho toàn hành trình
    current_gas = 0  # Lượng xăng tích lũy khi di chuyển qua các trạm
    start_index = 0  # Trạm bắt đầu

    for i in range(n):
        total_gas += gas[i] - distance[i]
        current_gas += gas[i] - distance[i]

        # Nếu tại một trạm, xăng tích lũy bị âm, không thể tiếp tục
        if current_gas < 0:
            # Thử bắt đầu từ trạm kế tiếp
            start_index = i + 1
            current_gas = 0  # Reset lượng xăng tích lũy

    # Nếu tổng lượng xăng tích lũy toàn hành trình >= tổng khoảng cách thì có thể hoàn thành hành trình
    return start_index if total_gas >= 0 else -1

    

# Ví dụ:
gas = [4, 6, 7, 4]
distance = [6, 5, 3, 5]
print("Start =", can_complete_circuit(gas, distance)+1)  # Kết quả đúng phải là Start = 1