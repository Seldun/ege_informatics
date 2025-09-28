# TODO: плагин на грамматику, плагин на отображение TODO   №3 скачать файлы TODO настроить PEP8

with open("ege/type_27/solutions/task_01/1A.txt") as f:
    n = f.readline() # Очень важная строчка, чтобы пропустить первую строчку (X Y\n)
    a = [[] for i in range(2)] # создаём 2 списка куда будем заносить звёзды по их кластеру
    for _ in range(999):
        star = list(map(float, f.readline().replace(',' , '.').split())) # каждую строчку превращаем в список с float X и Y (смотри чтобы первая строчка не была буквами)
        if star[0] > 0: # смотрим по иксу, 2 кластера находятся по разным сторонам Ох
            a[0].append(star) # правый в лево в [0]
        else:
            a[1].append(star) #  левый на право в [1]
    sum_x = sum_y = tx = ty = 0
    for cluster in a:
        mn = float("inf")
        for j in cluster:
            x1, y1 = j
            sm = 0
            for k in cluster:
                x2, y2 = k
                sm += ((x2-x1)**2 + (y2-y1)**2)**0.5 # если одна и также точка, то =0
            if sm < mn:
                mn = sm
                tx, ty = x1, y1
        sum_x += tx
        sum_y += ty
    print(int(sum_x / 2 * 10))
    print(int(sum_y / 2 * 10))