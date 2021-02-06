# v = 1秒間にvメール進む
# 投げた瞬間から t秒後 から s秒後まで消える魔球を投げれる
# d メートルの地点で離れていなければボールを打てる
v, t, s, d = map(int, input().split())

# n秒の時点で受け取る
n = d/v

if t > n or s < n :
    print('Yes')
else:
    print('No')
