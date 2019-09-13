#標準入力...input系

##標準入力では、input()よりもsys.stdin.readline()を使う方が処理時間が短い
from sys import stdin

input = stdin.readline()

## 一行のみの入力  ----------

#INPUT: abcde, OUTPUT: "abcde"
str = input()

#INPUT: abcde, OUTPUT: ['a','b','c','d','e']
li = list(input())

#INPUT: 5, OUTPUT: 5
i = int(input())

#INPUT: 1 2, OUTPUT: a=1, b=2
a, b = map(int, input().split())

#INPUT: 1 2 3 4 5 ... n , OUTPUT: ['1','2','3'...'n']
strli = input().split()

#INPUT: 1 2 3 4 5 ... n, OUTPUT: [1,2,3,...,n]
ili = list(map(int, input().split()))


## 複数行の入力  ----------

#INPUT: 3       OUTPUT: n=3, ['hoge','foo','bar']
#       hoge
#       foo
#       bar
n = int(input())
strli = [input() for i in range(n)]



#標準出力...print系
str = "hogehoge"
a = 1
b = 2

#INPUT: str="hogehoge", OUTPUT: hogehoge\n
print(str)

#INPUT: str="hogehoge", OUTPUT: hogehoge
print(str, end="")

#INPUT: a=1, b=2 , OUTPUT: 0.5\n
print(a/b)

#INPUT: a=1, b=2 , OUTPUT: 0.5です。\n
print((a/b)+'です。')

## 小数点表示 ------------

a = 0.364364

print(a) #0.364364
print("{:.6f}".format(a)) #0.364364
print("{:.4f}".format(a)) #0.3644 小数点第4位に丸めることもできる。

b = 810

print("{:b}".format(b)) #1100101010  2進数表記
print("{:o}".format(b)) #1452        8進数表記
print("{:x}".format(b)) #32a         16進数小文字表記
print("{:X}".format(b)) #32A         16進数大文字表記

## ゼロ埋め・幅寄せ -----------

print("python".ljust(15,'-')) # 左詰め
#python---------
print("python".center(15,'-'))# 中央寄せ
#-----python----
print("python".rjust(15,'-')) # 右詰め
#---------python

print(str(29).rjust(10,'0')) #10桁ゼロ埋め
#0000000029


##組み込み系

##リストやセットの全要素に対して条件分岐を行う

#全てがTrueか判定するall()
nums = [1,2,3,4,5,6,7,8,9,10]
if all(num%2 == 0 for num in nums):
    print("All True")
else:
    print("False is exist")
#どれか一つがTrueか判定するany()
nums = [1,2,3,4,5,6,7,8,9,10]
if any(num == 5 for num in nums):
    print("5 is exist")
else:
    print("All False")

##辞書・タプル・リストを要素にもつリストのソート
#全ての要素を順に比較する
a = [("b", 3), ("b", 1), ("a", 1), ("a", 2), ("c", 2)]
a.sort()
# OUTPUT: [('a', 1), ('a', 2), ('b', 1), ('b', 3), ('c', 2)]
#...１度ソートしたリストを別の要素に対してソートしたい場合に使える

#文字列操作 -----------------

#文字列リストの連結
chars = ['a','b','c','d','e','f','g']
new_str = ''.join(chars)

