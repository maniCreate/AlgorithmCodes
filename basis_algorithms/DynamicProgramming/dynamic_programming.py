
# Created at 2019.06.02
# 動的計画法

#動的計画法（DP）は以下の２種類が存在する
#  1.メモ化再帰(トップダウン)
#    ... 検索結果を記録（メモ）しておき、同じ数に関しては１度しか計算しない方法
#       → 探索木の親→子に向かって計算を進めていくやり方
#         = nから始めてn-1+n-2,n-2+n-3,....1+1という流れ
#  2.分割統治法+漸化式ループ(ボトムアップ)
#    ... nを求めるのに1+1から始め、nに達するまで繰り返し計算していく方法
#            = 同じ計算は１度しかしない＋メモリ消費が少ない
#       → 探索木の子→親に向かって進めていく, 1+1,1+2,2+3...n-2+n-1,nという流れ

#コード例）フィボナッチ数列
#1.メモ化再帰

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibnacchi1(n):
    if n <= 1: return 1
    else: return fibnacchi1(n-1)+fibnacchi1(n-2)

print(fibnacchi1(10))

# 2.分割統治法*漸化式ループ
def fibnacchi2(n):
    if n == 0:
        return 1
    else:
        fib1 = fib2 = fib3 = 1
        for i in range(n-1):
            fib3 = fib1+fib2
            fib1 = fib2
            fib2 = fib3
        return fib3

print(fibnacchi2(10))


# 3.メモ化（ボトムアップ）
def fibnacchi3(n):
    memo = [1,1]
    for i in range(1,n-1):
        memo.append(memo[i]+memo[i-1])
    return memo[n]

print(fibnacchi3(10))
