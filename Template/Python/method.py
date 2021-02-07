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

# トリム 前後の空白（スペース）
str = ' text '.strip()
print(str) # `text`

# トリム 先頭の空白のみ
str = ' text '.lstrip()
print(str) # `text `

# トリム 末尾の空白のみ
str = ' text'.rstrip()
print(str) # ` text`

# 特定の文字が含まれている位置 先頭から検索（特定の文字が含まれていない場合は、 -1 が返却される）
n = 'text'.find('a')
print(str) # 0

# 特定の文字が含まれている位置 先頭から検索（特定の文字が含まれていない場合は、 -1 が返却される）
n = 'text'.rfind('a')
print(str) # 3

# 特定の文字が含まれているか否か
str = 'text'
b1 = 't' in str
b2 = 't' in str and 'x' in str
print(b1) # True
print(b2) # True

# 特定の文字が含まれる回数
n1 = 'aaaabca'.count('a')
n2 = 'aaaabba'.count('aa')
print(n1) # 5
print(n2) # 2
