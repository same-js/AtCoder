a, b, c = map(int, input().split())

def get_name(c):
    if c == 0 :
        return "Aoki"
    else:
        return "Takahashi"

if (a - b) == 0 :
    # 差分が0の場合、勝者は c ではないほう
    print(get_name(c))

else :
    if a - b > 0 :
        print("Takahashi")
    else :
        print("Aoki")
