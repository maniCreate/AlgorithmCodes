#レーベンシュタイン距離問題

def levenshtein(str1, str2):

    if str1 == "":
        str1_len = 0
    else:
        str1_len = len(str1)

    if str2 == "":
        str2_len = 0
    else:
        str2_len = len(str2)

    dp = [[0 for _ in range(str2_len+1)] for _ in range(str1_len+1)]

    #str1×空文字初期化
    for str1_i in range(str1_len+1):
        dp[str1_i][0] = str1_i

    for str2_i in range(str2_len+1):
        dp[0][str2_i] = str2_i

    for line_i in range(1, str1_len+1):
        for column_i in range(1, str2_len+1):
            #現在地の左と上の値が等しいかどうか判定
            topValue = dp[line_i-1][column_i]
            leftValue = dp[line_i][column_i-1]
            topLeftValue = dp[line_i-1][column_i-1]

            if str1[line_i-1] == str2[column_i-1]:
                topLeftValue += 0
            else:
                topLeftValue += 1

            dp[line_i][column_i] = min(topValue+1, leftValue+1, topLeftValue)

    print(dp)

    return dp[str1_len][str2_len]

print(levenshtein("kitten","sitting"))
