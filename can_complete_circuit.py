def can_complete_circuit(gas, distance):
    n = len(gas)

    total_gas = 0
    current_gas = 0
    start_index = 0

    for i in range(n):
        total_gas += gas[i] - distance[i]
        current_gas += gas[i] - distance[i]

        if current_gas < 0:

            start_index = i + 1
            current_gas = 0

    return start_index if total_gas >= 0 else -1

    

# Ví dụ:
gas = [4, 6, 7, 4]
distance = [6, 5, 3, 5]
print("Start =", can_complete_circuit(gas, distance)+1)  