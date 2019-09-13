# 問題文
# 整数 A, B があります。
# A+B,  A−B,  A×B の中で最大の数を出力してください。

# 制約
# ・入力は全て整数である。
# ・−100≤A, B≤100

# 入力
# 入力は以下の形式で標準入力から与えられる。

# 「A B」

# 出力
# A+B,  A−B,  A×B の中で最大の数を出力せよ。

line = input().split()

a = int(line[0])
b = int(line[1])

print(max(a-b,a+b,a*b))