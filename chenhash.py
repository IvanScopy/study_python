class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Khởi tạo bảng băm với các ô là None (trống)

    def hash_function(self, x):
        return x % 10  # Hàm băm: lấy phần dư của x chia cho 10

    def quadratic_probe(self, key, i):
        # Thăm dò bậc hai: vị trí = (hàm băm + i^2) % size
        return (self.hash_function(key) + i * i) % self.size

    def insert(self, key):
        i = 0  # Chỉ số thử nghiệm ban đầu
        while i < self.size:
            # Tính toán vị trí của khóa với thăm dò bậc hai
            index = self.quadratic_probe(key, i)
            if self.table[index] is None:  # Nếu ô trống, chèn vào
                self.table[index] = key
                print(f"Chèn {key} vào vị trí {index}")
                return True
            else:
                print(f"Vị trí {index} đã có giá trị {self.table[index]}. Thử tiếp!")
            i += 1
        return False  # Nếu không tìm được vị trí, bảng đã đầy

    def display(self):
        print("Bảng băm hiện tại:")
        for i in range(self.size):
            print(f"Vị trí {i}: {self.table[i]}")


# Tạo bảng băm với kích thước 10
hash_table = HashTable(10)

# Dãy giá trị cần chèn vào bảng băm
values = [4371, 1323, 6173, 4199, 4344, 9679, 1989]

# Chèn từng giá trị vào bảng băm
for value in values:
    hash_table.insert(value)

# Hiển thị bảng băm
hash_table.display()
