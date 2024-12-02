class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Khởi tạo bảng băm với các ô trống
        self.count = 0

    def hash_function(self, key):
        # Hàm băm sử dụng phép toán modulo
        return hash(key) % self.size

    def quadratic_probe(self, key, i):
        # Thăm dò bậc 2, i là số lần thăm dò
        return (self.hash_function(key) + i ** 2) % self.size

    def insert(self, key, value):
        if self.count >= self.size // 2:  # Nếu bảng gần đầy, mở rộng bảng
            self.resize()

        i = 0
        while i < self.size:
            index = self.quadratic_probe(key, i)
            if self.table[index] is None:
                self.table[index] = (key, value)  # Thêm phần tử mới vào bảng
                self.count += 1
                return
            elif self.table[index][0] == key:  # Nếu khóa đã tồn tại, cập nhật giá trị
                self.table[index] = (key, value)
                return
            i += 1

        print("Bảng băm đầy, không thể thêm phần tử mới")

    def search(self, key):
        i = 0
        while i < self.size:
            index = self.quadratic_probe(key, i)
            if self.table[index] is None:  # Nếu ô trống, không có phần tử
                return None
            elif self.table[index][0] == key:  # Nếu tìm thấy khóa
                return self.table[index][1]
            i += 1
        return None  # Nếu không tìm thấy khóa

    def delete(self, key):
        i = 0
        while i < self.size:
            index = self.quadratic_probe(key, i)
            if self.table[index] is None:  # Nếu ô trống, không có phần tử
                return False
            elif self.table[index][0] == key:  # Nếu tìm thấy khóa
                self.table[index] = None  # Xóa phần tử
                self.count -= 1
                return True
            i += 1
        return False  # Nếu không tìm thấy khóa

    def resize(self):
        # Tăng kích thước bảng băm khi bảng đầy
        new_size = self.size * 2
        new_table = [None] * new_size
        for item in self.table:
            if item is not None:
                key, value = item
                i = 0
                while i < new_size:
                    index = (hash(key) + i ** 2) % new_size
                    if new_table[index] is None:
                        new_table[index] = (key, value)
                        break
                    i += 1
        self.size = new_size
        self.table = new_table

    def __repr__(self):
        return str(self.table)


# Minh họa cài đặt:
ht = HashTable(10)
ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("grape", 7)

print("Bảng băm sau khi thêm phần tử:")
print(ht)

# Tìm kiếm phần tử
print("Tìm kiếm 'banana':", ht.search("banana"))

# Xóa phần tử
ht.delete("banana")
print("Bảng băm sau khi xóa 'banana':")
print(ht)

# Thử thêm phần tử và kiểm tra
ht.insert("pear", 9)
ht.insert("cherry", 6)
print("Bảng băm sau khi thêm 'pear' và 'cherry':")
print(ht)
