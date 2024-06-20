def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

def get_suggestions(word, dictionary):
    suggestions = []
    for dict_word in dictionary:
        distance = edit_distance(word, dict_word)
        if distance <= 2:  # Tolerance level for spelling correction
            suggestions.append((distance, dict_word))
    suggestions.sort(key=lambda x: x[0])
    return [word for _, word in suggestions]
