def longest_str_chain(words):
    # Sắp xếp các từ theo độ dài
    words.sort(key=len)

    # Mảng dp để lưu độ dài chuỗi từ dài nhất kết thúc tại mỗi từ
    dp = {word: 1 for word in words}

    # Kiểm tra mọi cặp từ trong danh sách đã sắp xếp
    for word in words:
        for i in range(len(word)):
            prev_word = word[:i] + word[i+1:]  # Tạo từ con
            if prev_word in dp:
                dp[word] = max(dp[word], dp[prev_word] + 1)

    # Trả về độ dài của chuỗi từ dài nhất
    return max(dp.values())

# Ví dụ
words = ["a", "b", "ba", "bca", "bda", "bdca"]
result = longest_str_chain(words)
print(result)  # Kết quả là 4
