# 単一の 整数 入力
a = int(input())

# 単一の 文字列 入力
s = input()

# スペース区切りの 整数 入力を 個別の変数 で受取（入力数/行 が固定の場合に）
b, c = map(int, input().split())

# スペース区切りの 整数 を配列 で受取
nums = list(map(int, input().split()))

# スペース区切りの 文字列 を 配列 で受取
strs = input().split() # s[0]でアクセス可能

# 出力方法
print("{} {}".format(a+b+c, s))
