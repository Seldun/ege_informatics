def f(A,x):
    return None


for A in range(1,1000):
    if all(f(x, A) == 1 for x in range(1, 1000)):
        print(A)