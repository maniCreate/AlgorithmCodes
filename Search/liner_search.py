
# Created at 2019.06.02
# 線形探索アルゴリズム
# 目的のデータを、全データ群の中から１つ１つチェックして探し出すアルゴリズム＝全探索

# MARK:- 線形探索アルゴリズムは全探索するためデータ量が膨大になった場合には非効率。
#最大探索回数は N (データの個数分), 平均探索回数は N/2 となる。
# →100万個のデータを探索する場合、最大探索回数は 100万回, 平均50万回探索することになる。

def liner_search(card_list, get_card):
    for i,element in enumerate(card_list):
        if element == get_card:
            print("{0}番目に{1}はあります".format(i+1,get_card))
            return
    print("{0}はありませんでした".format(get_card))

if __name__ == '__main__':
    cards = ["h-5","h-J","h-2","h-9","h-1","h-7","h-K","h-4","h-10","h-3","h-6","h-8","h-Q"]
    target_card = "h-K"
    liner_search(cards,target_card)
