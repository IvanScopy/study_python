class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Chèn xâu vào Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Tìm kiếm tiền tố chung dài nhất
    def longest_common_prefix(self, words):
        for word in words:
            self.insert(word)

        node = self.root
        prefix = ""

        while node and len(node.children) == 1 and not node.is_end_of_word:
            char, next_node = list(node.children.items())[0]
            prefix += char
            node = next_node

        return prefix


# Ví dụ sử dụng:
words = ["flower", "flow", "flight"]
trie = Trie()

# Chèn các xâu vào Trie
for word in words:
    trie.insert(word)

# Tìm kiếm tiền tố chung dài nhất
common_prefix = trie.longest_common_prefix(words)
print("Longest Common Prefix:", common_prefix)
