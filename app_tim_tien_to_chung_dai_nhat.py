class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def longest_common_prefix(self):
        prefix = ""
        node = self.root
        # Duyệt qua cây từ gốc, tìm tiền tố chung
        while node and len(node.children) == 1 and not node.is_end_of_word:
            for char in node.children:
                node = node.children[char]  # Đi tới nút con duy nhất
                prefix += char
                break  # Dừng lại sau khi lấy nút con đầu tiên

        return prefix


# Tạo cây Trie và chèn các từ
trie = Trie()
words = ["the", "a", "an", "there", "answer", "any", "by", "bye", "their"]

for word in words:
    trie.insert(word)

# Tìm kiếm các từ trong cây
search_words = ["the", "those", "there", "their", "tho"]
print("Kết quả tìm kiếm:")
for word in search_words:
    print(f"'{word}': {'Có' if trie.search(word) else 'Không'}")

# Tìm tiền tố chung dài nhất
longest_prefix = trie.longest_common_prefix()
print("\nTiền tố chung dài nhất:", longest_prefix if longest_prefix else "Không có tiền tố chung")
