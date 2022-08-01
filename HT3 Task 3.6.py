def int_func():
    list_words = input("Введите несколько слов строчными латинскими буквами: ").lower().split()
    for word in list_words:
        items = 0
        for item in word:
            if ord(item) >= 97 and ord(item) <= 122:
                items += 1

        print(word.title() if items == len(word) else f'{list_words} only small latin letters')

print(int_func())



