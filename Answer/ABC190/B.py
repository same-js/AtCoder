# 勝利条件：1度でもダメージを与えればよい
# ダメージを与えられた場合は、Yes、与えられない場合は No

# n=魔法の数、s=これ以上の秒数の呪文ではダメージなし、 d=これ以下の威力の呪文ではダメージなし
n,s,d = map(int, input().split())

hit = False
for i in range(n):
    # x=詠唱時間（秒）、y=威力
    x, y = map(int, input().split())

    if s > x and d < y :
        hit = True
        break

if hit == True :
    print('Yes')
else:
    print('No')
