for x in range(3001): # можно перевернуть и добавить break, тогда будет лучше
    a = 9 * 11**210 + 8*11**150 - x
    cnt = 0
    while a > 0:
        if a % 11 == 0:
            cnt += 1
        a //= 11

    if cnt == 60:
        print(x)