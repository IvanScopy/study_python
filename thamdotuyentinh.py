class HashTableLinearProbing:
    def __init__(self, size=23):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Cập nhật giá trị nếu từ đã tồn tại
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return "Không tìm thấy"

# Tạo từ điển
dictionary_linear = HashTableLinearProbing()

# Chèn từ vào từ điển
dictionary_linear.insert("apple", "quả táo")
dictionary_linear.insert("book", "cuốn sách")
dictionary_linear.insert("apple", "táo")

# Tìm kiếm
print(dictionary_linear.search("apple"))  # Output: táo
print(dictionary_linear.search("book"))   # Output: cuốn sách
print(dictionary_linear.search("cat"))    # Output: Không tìm thấy
