# 問題文
# 高橋くんは N 種類の料理が食べ放題のビュッフェに行き、全種類の料理 (料理 1, 料理 2, …, 料理 N) を 1 度ずつ食べました。
# 高橋くんが i (1≤i≤N) 番目に食べた料理は料理 Ai でした。
# 高橋くんは、料理 i (1≤i≤N) を食べると満足度 Bi を得ます。
# また、料理 i (1≤i≤N−1) を食べた直後に料理 i+1 を食べると満足度 Ci を追加で得ます。

# 高橋くんが得た満足度の合計を求めてください。

# 制約
# ・入力は全て整数である。
# ・2≤N≤20
# ・1≤Ai≤N
# ・A1,A2,...,AN は全て異なる。
# ・1≤Bi≤50
# ・1≤Ci≤50

# 入力
# 入力は以下の形式で標準入力から与えられる。
# -------------
# N
# A1 A2 ... AN
# B1 B2 ... BN
# C1 C2 ... CN−1
# -------------

# 出力
# 高橋くんが得た満足度の合計を整数で出力せよ。

n = int(input())

meals = list(map(int, input().split()))
likes = list(map(int, input().split()))
addLikes = list(map(int, input().split()))

total_like = 0

for i in range(n):
  meal = meals[i]
  like = likes[meal-1]
  if i < n-1 and meal == meals[i+1]-1:
    like += addLikes[meal-1]
  total_like += like

print(total_like)