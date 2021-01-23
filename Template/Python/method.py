# 繰返 n:繰り返し回数 i:カウンタ
for i in range(n):
    print(n)

# 繰返 配列
l = ['A', 'B', 'C']
for name in l:
    print(name)

# 重複する配列 重複を削除
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
unique = set(l)
print(unique) # ['a', 'b', 'c']

# 重複する配列 重複している回数 単一
l.count(1)

# 重複する配列 重複している回数 一括
import collections
c = collections.Counter(l)
print(c) # Counter({'a': 4, 'c': 2, 'b': 1})
print(c['a']) # 4
