def are_similar(str1, str2):
    # Nếu hai chuỗi giống nhau, chúng tự nhiên là tương tự nhau
    if str1 == str2:
        return True
    # Tìm các vị trí có sự khác biệt
    diff = []
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff.append(i)
            # Nếu có hơn 2 vị trí khác nhau, không thể hoán đổi 2 ký tự
            if len(diff) > 2:
                return False
    # Kiểm tra nếu hoán đổi hai ký tự là có thể
    return len(diff) == 2 and str1[diff[0]] == str2[diff[1]] and str1[diff[1]] == str2[diff[0]]


def find_groups(A):
    n = len(A)
    visited = [False] * n
    groups = 0

    def dfs(index):
        visited[index] = True
        for i in range(n):
            if not visited[i] and are_similar(A[index], A[i]):
                dfs(i)

    for i in range(n):
        if not visited[i]:
            groups += 1
            dfs(i)

    return groups


# Ví dụ:
A = ["tars", "rats", "arts", "star"]
print(find_groups(A))  # Output: 2
