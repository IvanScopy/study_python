class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Khởi tạo bảng băm với các ô trống
        self.count = 0

    def hash_function(self, key):
        # Hàm băm sử dụng phép toán modulo để tính chỉ số
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index  # Giữ lại vị trí ban đầu để kiểm tra thăm dò tuyến tính

        # Thăm dò tuyến tính để tìm ô trống hoặc ô với cùng khóa
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size  # Chuyển sang ô kế tiếp (theo tuyến tính)
            if index == original_index:  # Nếu quay lại ô đầu tiên thì bảng đã đầy
                raise Exception("Hash table is full")

        # Thêm phần tử vào bảng băm
        self.table[index] = (key, value)
        self.count += 1

    def search(self, key):
        index = self.hash_function(key)
        original_index = index

        # Thăm dò tuyến tính để tìm kiếm phần tử
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Trả về giá trị nếu tìm thấy
            index = (index + 1) % self.size  # Tiến sang ô kế tiếp theo tuyến tính
            if index == original_index:
                break  # Nếu quay lại vị trí ban đầu, tức là đã duyệt hết bảng

        return None  # Không tìm thấy phần tử

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index

        # Thăm dò tuyến tính để tìm phần tử cần xóa
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Xóa phần tử tại vị trí này
                self.count -= 1
                return True
            index = (index + 1) % self.size  # Tiến sang ô kế tiếp theo tuyến tính
            if index == original_index:
                break  # Nếu quay lại vị trí ban đầu, tức là đã duyệt hết bảng

        return False  # Không tìm thấy phần tử để xóa

    def display(self):
        for index, item in enumerate(self.table):
            if item is not None:
                print(f"Index {index}: Key = {item[0]}, Value = {item[1]}")
            else:
                print(f"Index {index}: Empty")


# Sử dụng HashTable
hash_table = HashTable(10)

# Thêm phần tử vào bảng băm
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

# Tìm kiếm phần tử trong bảng băm
print("Search apple:", hash_table.search("apple"))  # Output: 10
print("Search banana:", hash_table.search("banana"))  # Output: 20

# Hiển thị bảng băm
hash_table.display()

# Xóa phần tử khỏi bảng băm
hash_table.delete("banana")
print("After deleting banana:")
hash_table.display()

# Tìm kiếm phần tử sau khi xóa
print("Search banana:", hash_table.search("banana"))  # Output: None
