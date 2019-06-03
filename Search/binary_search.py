
# Created at 2019.06.02
# 二分探索アルゴリズム
# ソート済のデータ群を２つに分割し、目的のデータが
# 分割したデータ群のどちらに含まれているかを繰り返して探索するアルゴリズム

# MARK:- データがソート済であることが条件→バラバラであればデータをソートする必要がある→ソートアルゴリズム
#最大探索回数は log2N+1, 平均探索回数は log2N となる。
# →100万個のデータを探索する場合、最大探索回数は 21回, 平均20回の探索で済む。

def binary_search(card_list,get_card):
    low = 0
    high = len(card_list)-1
    while low <= high:
        mid = (low+high)//2
        if card_list[mid] == get_card:
            print("{0}番目に{1}はあります".format(mid,get_card))
            return
        elif card_list[mid] < get_card:
            low = mid + 1
        else:
            high = mid - 1
    return

if __name__ == '__main__':
    heart_cards = [1,2,4,5,6,8,9,10,12,13]
    heart_eight = 8
    binary_search(heart_cards, heart_eight)
