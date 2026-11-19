import random

# Ввод размеров матрицы r (строки) и c (столбцы) от 2 до 12
r = int(input("Введите количество строк R (от 2 до 12): "))
c = int(input("Введите количество столбцов C (от 2 до 12): "))

if not (2 <= r <= 12 and 2 <= c <= 12):
    print("Ошибка: размеры должны быть от 2 до 12.")
else:
    ch = input("Заполнение (1 - по порядку от 1, 2 - случайно от 1 до 50): ")
    # Создаём матрицу m
    m = []
    k = 1
    for i in range(r):
        row = []
        for j in range(c):
            if ch == "1":
                row.append(k)
                k += 1
            else:
                row.append(random.randint(1, 50))
        m.append(row)

    # Вывод исходной матрицы таблицей
    print("\nИсходная матрица:")
    for row in m:
        for x in row:
            print(f"{x:4}", end="")
        print()

    #  Сумма и произведение по строкам (sr, pr) и по столбцам (sc, pc)
    sr = []
    pr = []
    for i in range(r):
        s = 0
        p = 1
        for j in range(c):
            s=s+m[i][j]
            p=p*m[i][j]
        sr.append(s)
        pr.append(p)

    sc = []
    pc = []
    for j in range(c):
        s = 0
        p = 1
        for i in range(r):
            s=s+m[i][j]
            p=p*m[i][j]
        sc.append(s)
        pc.append(p)

    print("\nПо строкам:")
    for i in range(r):
        print(f"Строка {i + 1}: сумма = {sr[i]}, произведение = {pr[i]}")

    print("\nПо столбцам:")
    for j in range(c):
        print(f"Столбец {j + 1}: сумма = {sc[j]}, произведение = {pc[j]}")
    # Строка и столбец с максимальной суммой
    a= sr.index(max(sr)) + 1
    b = sc.index(max(sc)) + 1
    print(f"\nМакс. сумма в строке №{a} ({max(sr)}) и в столбце №{b} ({max(sc)})")
    # обмен первой и последней строк, первого и последнего столбцов
    # Копия матрицы
    m2 = [row[:] for row in m]        
    m2[0],m2[-1] = m2[-1],m2[0]
    for row in m2:
        row[0],row[-1] = row[-1], row[0]
    print("\nПосле обмена крайних строк и столбцов:")
    for row in m2:
        for x in row:
            print(f"{x:4}", end="")
        print()
    # Транспонирование 
    mt=[]
    for j in range(c):
        row = []
        for i in range(r):
            row.append(m[i][j]) 
        mt.append(row)
    print("\nТранспонированная матрица:")
    for row in mt:
        for x in row:
            print(f"{x:4}", end="")
        print()
    if r == c:
        if m == mt:
            print("Равна транспонированная исходной")
        else:
            print("Не равна")
    # Поиск «седловых точек» 
    sp = []
    for i in range(r):
        for j in range(c):
            x = m[i][j]
            # Собираем элементы текущего j-го столбца в отдельный список col
            col = [m[k][j] for k in range(r)]
            if (x == min(m[i]) and x == max(col)) or (x == max(m[i]) and x == min(col)):
                sp.append((i + 1, j + 1, x))

    print("\nСедловые точки (строка, столбец, значение):", sp if sp else "нет")
    # Уникальные элементы по возрастанию 
    u = []
    for row in m:
        for x in row:
            if x not in u:
                u.append(x)
    u.sort()
    print("Уникальные элементы по возрастанию:", u)

    #  След матрицы (tr) для квадратной матрицы
    if r == c:
        tr = sum(m[i][i] for i in range(r))
        print(f"След матрицы (сумма главной диагонали): {tr}")