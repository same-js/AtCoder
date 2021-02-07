# 公式解説の解法

# = n の長さの整数列、 x = 除外する整数
n, x = map(int, input().split())
a = list(map(int, input().split()))

print(" ".join([str(i) for i in a if i != x]))
