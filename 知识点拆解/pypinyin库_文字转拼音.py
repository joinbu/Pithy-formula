import pypinyin as py
word = '朝阳'

A = py.pinyin(word, heteronym=True) #含声调
B = py.lazy_pinyin(word)	#不含声调

print(A)
print(B)