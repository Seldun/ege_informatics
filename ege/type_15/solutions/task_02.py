def f(x, y, A):
    return None


for A in range(0, 1000): # точки, с 2 неизвестными
    if all(f(x, y, A) == 1 for x in range(1,100) for y in range(1,100)):
        print(A)
        break