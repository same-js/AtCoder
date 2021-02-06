# 時間切れにつき未完成

# h=行数 w=列数
h, w = map(int, input().split())

slist = []

angle = 0
s_angle = 0
e_angle = 0
v_s = 0
v_e = 0

old_start = 0
old_end   = 0

m = 0 # 多角形が始まっていれば1になる

for i in range(h+1):

    # 最後まで回っている場合、天辺をたすかどうかの判断だけして終了
    if i == h :
        if old_end - old_start > 1: # つまり2以上の場合
            angle += 1 # 天辺が一角形 保証される
            break


    s = input()
    # 端と端を拾う
    start = s.find('#')
    end   = s.rfind('#')

    if start == -1 and end == -1 and m == 0 :
        continue


    if m == 0:
        if end - start > 1: # つまり2以上の場合
            angle += 1 # 天辺が一角形 保証される
    if m == 1:
        # 方向だけ取得、必ず2加算
        angle += 2
        if old_start > start:
            v_s = -1
        elif old_start < start:
            v_s = 1
        if old_end > end:
            v_e = -1
        elif old_end < end:
            v_e = 1
        #print('M=1:' + str(old_end) + '|' + str(end))

    if i > 1:
        # 多角形の最後まで辿りついた場合
        #print(str(start) + '|' + str(end))
        if start == -1 and end == -1:
            # print("test:" + str(old_end) + '|' + str(old_start))
            if old_end - old_start > 1: # つまり2以上の場合
                angle += 1 # 天辺が一角形 保証される
                break

        # 同じ方向に進んでいる限りは、無視
        if old_start > start and v_s in (0, 1):
            s_angle += 1
            v_s = -1
        elif old_start < start and v_s in (0, -1):
            s_angle += 1
            v_s = 1
        elif old_start == start and v_s in (-1, 1):
            s_angle += 1
            v_s = 0

        if old_end > end and v_e in (0, 1):
            e_angle += 1
            v_e = -1
        elif old_end < end and v_e in (0, -1):
            e_angle += 1
            v_e = 1
        elif old_end == end and v_e in (-1, 1):
            #print("e|v_e=" + str(v_s))
            e_angle += 1
            v_e = 0

        # if i == h-1 :
        #     if end - start > 1: # つまり2以上の場合
        #         angle += 1 # 天辺が一角形 保証される

    old_start = start
    old_end   = end
    m += 1
    #print(v_s)
print('---')
print(angle)
print(s_angle)
print(e_angle)
