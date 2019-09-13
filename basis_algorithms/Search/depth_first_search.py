
# Created at 2019.06.02
# 深さ優先探索アルゴリズム
# 探索木やグラフから任意の条件に合致するグラフ（ノード）を、
# 深さを優先（子のないノードに到達するまで）して検索するアルゴリズム

# 深さ優先探索の主な使い所
# ・与えられた迷路/マップのゴールまでの最短距離を求める時
# ・与えられた迷路/マップで、同じ道を通らずにゴールまで到達するルートを全て求める時
#  etc....

# 深さ優先探索を用いるべきケース
# 1. 全通りのパターンを列挙し、結果をまとめる必要がある場合
# 2. 文字列などを探索するときに、辞書順であることが求められる場合

# 深さ優先探索の実装方法
#   → スタックを用いる
# 1.スタックを用意する
# 2.スタックに最初の要素を入れる(push)
# 3.スタックから要素を取り出す(pop)
# 4.要素に対して処理をする
# 5.要素の子供をスタックに入れる(push)
# 6.スタックがカラになるまで3～5を繰り返す

def get_map_info(map = ""):
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


def search_route_pattern(map = ""):
    #ルート数を計算するマップを取得
    map_info = get_map_info(map)
    #
    map_passed = [[False for j in range(map_info['width'])] for i in range(map_info['height'])]

    return search_route_recursion(map_info['startX'], map_info['startY'], map_info, map_passed)


def search_route_recursion(x, y, map_info, map_passed):

    #マップの移動パターン
    move_x = [1, -1, 0,  0]
    move_y = [0,  0, 1, -1]
    #移動パターンの数
    move_pattern = len(move_x)
    #ルート数の結果
    count = 0

    #ゴールに到達した場合
    if (x == map_info['targetX'] and y == map_info['targetY']):
        # 全ての道を通過した判定をする場合はコメントを外す
        """
        map_passed[x][y] = True
        for i in range(map_info['width']):
            for j in range(map_info['height']):
                if not map_passed[i][j]:
                    return 0
        """
        return 1

    #範囲内、未踏、かつゴールに到達していない場合
    if (0 <= x and x < map_info['width']) and (0 <= y and y < map_info['height']) :
        passed = map_passed[x][y]
        if not passed:
            map_passed[x][y] = True
            for i in range(move_pattern):
                count += search_route_dfs_recursion(x+move_x[i], y+move_y[i], map_info, map_passed)
            map_passed[x][y] = False #走査が終わった道は初期化する

    return count


def main():

    map = [
            "...",
            "...",
            "..."
        ]

    pattern = search_route_pattern(map)
    print(u'ゴールまでのルートの数 : '+ str(pattern) )

if __name__ == "__main__":
    main()
