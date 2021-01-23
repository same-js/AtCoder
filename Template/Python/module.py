# 正確な計算を行う
from decimal import Decimal
a = Decimal(30)* Decimal(13/100)
b = 30 * 13/100
print('Decimal:' + a + '|Pure:' + b)
