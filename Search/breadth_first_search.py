
# Created at 2019.06.02
# 幅優先探索アルゴリズム
# 探索木やグラフから任意の条件に合致するグラフ（ノード）を、
# 幅を優先（進んだ先の階層に存在する子ノードを全て探索するまで）して検索するアルゴリズム

# 幅優先探索の主な使い所 = 最も条件に近いもの１つを求める場合に有利
# ・与えられた迷路/マップのゴールまでの最短距離を求める時 = 幅優先が有利
# ・与えられた迷路/マップで、同じ道を通らずにゴールまで到達するルートを全て求める時
#   =全探索になるため幅優先でも深さ優先でもさほど変わらない。
#  etc....

# 幅優先探索を用いるべきケース
# ・始点から最も近いものを求めたいケース
#    =条件に最初に合致したものが、全体で条件に最も合致しているという性質がある
# ・探索範囲は広いが、ある程度近くに求めたい解が存在することがわかっているケース
# ・探索範囲が広く、深さ優先探索ではスタックが大量に使われてしまうケース
#  etc....

# 幅優先探索の実装方法
#  → Queue（キュー）を用いる
# 1.根ノードを空のキューに加える。
# 2.ノードをキューの先頭から取り出し、以下の処理を行う。
#  ・ノードが探索対象であれば、探索をやめ結果を返す。
#  ・そうでない場合、ノードの子で未探索のものを全てキューに追加する。
# 3.もしキューが空ならば、グラフ内の全てのノードに対して処理が行われたので、探索をやめ”not found”と結果を返す。
# 4.2に戻る。

import queue
import time

def get_map_info(map):
    map_width = len(map[0])
    map_height = len(map)
    map_info = {
    #マップの座標を数値化
    'width':map_width,
    'height':map_height,
    #スタート地点の設定
    'startX':0,
    'startY':0,
    #ゴール地点の設定（0から始まるので-1）
    'targetX':map_height-1,
    'targetY':map_width-1
    }
    return map_info

def search_shortest_distance(map):
    #マップの移動パターン
    move_x = [1, -1, 0,  0]
    move_y = [0,  0, 1, -1]
    #移動パターンの数
    move_pattern = len(move_x)
    #最短距離を計算するマップを取得
    map_info = get_map_info(map)
    #地点毎に経過歩数を記録する多次元配列
    map_passed = [[-1 for j in range(map_info['width'])] for i in range(map_info['height'])]

    count = 0

    # Queueを利用していることを解りやすくするためにQueueモジュールを使ってますが、listのappend()とpop()で同じことできます。
    # Queue（先入先出）を生成
    queue_x = queue.Queue()
    queue_y = queue.Queue()
    #スタート位置をQueueに挿入
    queue_x.put(map_info['startX'])
    queue_y.put(map_info['startY'])
    #
    map_passed[map_info['startX']][map_info['startY']] = 0

    #Queueからデータが無くなるまで処理を繰り返す
    while not queue_x.empty():
        #現在地点を取得 = 親ノード
        x = queue_x.get()
        y = queue_y.get()

        #全てのパターンで検証 = 子ノードを幅探索していく
        for pattern in range(move_pattern):
            #検証する座標
            nextX = x + move_x[pattern]
            nextY = y + move_y[pattern]

                # 0<=nextX + nextX < map_width ...マップの横軸範囲内
                # 0<=nextY + nextX < map_height ... マップの縦軸範囲内
            if  (0 <= nextX) and (nextX < map_info['width']) and ( 0 <= nextY) and (nextY < map_info['height']):
                #次の座標が範囲内であれば保持して次の条件へ
                passed = map_passed[nextX][nextY]
                #次の地点がゴールならば...
                if ( nextX == map_info['targetX'] and nextY == map_info['targetY'] ):
                    # 経過距離の記録だけを行う
                    map_passed[nextX][nextY] = map_passed[x][y] + 1
                #次の地点がゴールでない & 未踏の地点ならば...
                if not( nextX == map_info['targetX'] and nextY == map_info['targetY'] ) and passed == -1:
                    # 次の地点に経過距離の記録を行う
                    map_passed[nextX][nextY] = map_passed[x][y] + 1
                    # ゴールではないので、Queueに追加してさらに検証
                    queue_x.put(nextX)
                    queue_y.put(nextY)

    for i in range(len(map_passed)):
        if max(map_passed[i]) >= count: count = max(map_passed[i])

    return count

def main():
    map = [
            "...",
            "...",
            "..."
        ]

    pattern = search_shortest_distance(map)
    print('最短歩数 : ' + str(pattern) )

if __name__ == "__main__":
    main()

#出力結果
# 最短歩数：4
# map = [
#         "0 1 2",
#         "1 2 3",
#         "2 3 4"
#     ]
