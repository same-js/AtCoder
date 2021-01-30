# 時間切れにつき未完成

# n = nの番号がついたn個の皿
# m = mの番号がついたm個の条件
n,m = map(int, input().split())

ms = []

for i in range(m):
# 条件i 皿a と 皿b の両方にボールが置かれている場合に条件を満たす
    a, b = map(int, input().split())
    ms.append([a,b])
    print(ms[i])

# k=人数
k = int(input())

for i in range(k):
    c,d = map(int, input().split())
    ks.append([c,d])

for i range(2**k):
    # 二進数で管理
    x = (bin())
    for j range(2):
