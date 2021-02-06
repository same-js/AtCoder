# = n の長さの整数列 x 整数
n, x = map(int, input().split())

# スペース区切りの 整数 を 配列 で受取
nums = input().split() # s[0]でアクセス可能
result = ''

for num in nums:
    if int(num) != x:
        result += num + ' '
print( result.strip() )
