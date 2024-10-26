class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=23):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value  # Cập nhật giá trị nếu từ đã tồn tại
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

# Sử dụng bảng băm dây chuyền
dictionary_chaining = HashTableChaining()

# Chèn từ vào từ điển
dictionary_chaining.insert("apple", "quả táo")
dictionary_chaining.insert("book", "cuốn sách")
dictionary_chaining.insert("apple", "táo")

# Lấy nghĩa tiếng Việt của từ
print(dictionary_chaining.search("apple"))  # Output: táo
print(dictionary_chaining.search("book"))   # Output: cuốn sách
print(dictionary_chaining.search("cat"))    # Output: None

