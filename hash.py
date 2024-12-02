class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Mảng bảng băm với mỗi ô là một danh sách rỗng

    def hash(self, x):
        return x % 10  # Hàm băm: lấy phần dư khi chia cho 10

    def insert(self, x):
        index = self.hash(x)
        self.table[index].append(x)  # Chèn giá trị vào danh sách tại ô bảng băm tương ứng

    def display(self):
        print("Bảng băm dây chuyền:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()

class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Mảng bảng băm với mỗi ô là None (trống)

    def hash(self, x):
        return x % 10  # Hàm băm: lấy phần dư khi chia cho 10

    def insert(self, x):
        index = self.hash(x)
        original_index = index
        # Tìm ô trống (xử lý xung đột bằng thăm dò tuyến tính)
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Thăm dò tuyến tính (di chuyển đến ô tiếp theo)
            if index == original_index:  # Nếu quay lại vị trí ban đầu, bảng đã đầy
                raise Exception("Bảng băm đã đầy")
        self.table[index] = x  # Chèn giá trị vào ô trống

    def display(self):
        print("Bảng băm thăm dò tuyến tính:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()

class HashTableQuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Mảng bảng băm với mỗi ô là None (trống)

    def hash(self, x):
        return x % 10  # Hàm băm: lấy phần dư khi chia cho 10

    def insert(self, x):
        index = self.hash(x)
        i = 1
        original_index = index
        # Tìm ô trống (xử lý xung đột bằng thăm dò bậc hai)
        while self.table[index] is not None:
            index = (original_index + i ** 2) % self.size  # Thăm dò bậc hai (di chuyển đến ô tiếp theo)
            i += 1
            if i > self.size:  # Nếu đã thử hết các vị trí trong bảng
                raise Exception("Bảng băm đã đầy")
        self.table[index] = x  # Chèn giá trị vào ô trống

    def display(self):
        print("Bảng băm thăm dò bậc hai:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()


# Dãy giá trị cần chèn vào bảng băm
values = [4371, 1323, 6173, 4199, 4344, 9679, 1989]

# a) Bảng băm dây chuyền
ht_chaining = HashTableChaining(10)
for value in values:
    ht_chaining.insert(value)
ht_chaining.display()

# b) Bảng băm thăm dò tuyến tính
ht_linear = HashTableLinearProbing(10)
for value in values:
    ht_linear.insert(value)
ht_linear.display()

# c) Bảng băm thăm dò bậc hai
ht_quadratic = HashTableQuadraticProbing(10)
for value in values:
    ht_quadratic.insert(value)
ht_quadratic.display()
