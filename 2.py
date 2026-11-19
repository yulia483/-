s = input("Введите текст: ")
# 1. Подсчёт слов на гласную (v) и на согласную (c)
gl = set("аеёиоуыэюяaeiouy")
sg = set("бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz")
# Очищаем строку от знаков препинания и разбиваем на список слов
t = "".join(ch if ch.isalpha() else " " for ch in s.lower())
w = t.split()
v = 0  
c = 0  #
for x in w:
    if x[0] in gl:
        v += 1
    elif x[0] in sg:
        c += 1
print(f"Слов с гласной: {v}, c cогласной: {c}")
# Самое частое слово и его частота
if len(w) > 0:
    d = {}
    for x in w:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    mx = max(d.items(), key=lambda item: item[1])
    print(f"Самое частое слово: «{mx[0]}» (встречается {mx[1]} раз)")
else:
    print("В тексте не найдено слов.")
#  Удаление повторяющихся подряд символов (сжатие в список r)
r = []
for ch in s:
    if len(r) == 0 or r[-1] != ch:
        r.append(ch)
print(f"После сжатия повторов: {''.join(r)}")
# Проверка на анаграмму со второй строкой s2
s2 = input("Введите вторую строку для проверки на анаграмму: ")
a1 = sorted([ch for ch in s.lower() if ch.isalpha()])
a2 = sorted([ch for ch in s2.lower() if ch.isalpha()])
if a1 == a2:
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")
#  Извлечение подстрок в кавычках «» или "" в список 
# Список для найденных фраз в кавычках
q = []  
i = 0  
while i < len(s):
    if s[i] == "«":
        j = s.find("»", i + 1)  
        if j != -1: 
            # Вырезаем всё между кавычками срезом
            q.append(s[i + 1 : j])  
            i = j              
    elif s[i] == '"':
        j = s.find('"', i + 1)  
        if j != -1:
            q.append(s[i + 1 : j])
            i = j
    i += 1
print("Подстроки в кавычках:", q)
#  Игра «Быки и коровы» для двух строк x и y одинаковой длины
x = input("Введите первую строку для игры «Быки и коровы»: ")
y = input("Введите вторую строку (такой же длины): ")
if len(x) != len(y):
    print("Ошибка: строки должны быть одинаковой длины.")
else:
    bk = 0  
    # Остаток первой строки
    rx = [] 
     # Остаток второй строки
    ry = []  
    for c1, c2 in zip(x, y):
        if c1 == c2:
            bk += 1
        else:
            rx.append(c1)
            ry.append(c2)
    kr = 0    
    for ch in rx:
        if ch in ry:
            kr += 1
            ry.remove(ch)

    print(f"Быки и коровы для «{x}» и «{y}»: быки={bk}, коровы={kr}")