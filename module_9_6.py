
def all_variants(text):
    len_text = len(text)  # 3 (длина текста)
    for i in range(1, len_text + 1):  # длина подстроки
        #print(i)
        for j in range(len_text - i + 1):
            yield text[j: j + i]


a = all_variants("abc")
for i in a:
    print(i)

