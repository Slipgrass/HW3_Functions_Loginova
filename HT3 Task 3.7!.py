#Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
#пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
#исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
#написанную ранее функцию int_func().

def int_func():
    for word in phrase:
        items = 0
        for item in word:
            if ord(item) >= 97 and ord(item) <= 122:
                """Проверяет принадлежнось каждого символа к латинским"""
                items += 1
                """Прибaваляет проверенный элемент к остальным, если цикл прошёл"""

                print(phrase.title() if items == len(phrase) else f'{phrase} only small latin letters')
                """Если все слова прошли цикл успешно, то печатает их с заглавной,
        
                если нет - прекращает работу и выдаёт сообщение
        
                """

phrase = input("Введите фразу строчными латинскими буквами: ")
for i in phrase:
    result = int_func()
    #if result:
        #print(result, ' ')




