p = list(range(25,65))
q = list(range(40,116))
a = []
for x in range(1, 1000):
    P = x in p
    Q = x in q
    A = x in a
    if (P <= ((Q and (not(A))) <= (not(P)))) == 0:
        a.append(x)

print(len(a) - 1) # так как это длина отрезка, кол запятых