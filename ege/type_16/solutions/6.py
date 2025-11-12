'''6.	Алгоритм вычисления функции F(n) задан следующими соотношениями:
		F(n) =  n · n + 5 · n + 4, при n > 30
		F(n) = F(n+1) + 3 · F(n+4), при чётных n  30
		F(n) = 2 · F(n+2) +  F(n+5), при нечётных n  30
Определите количество натуральных значений n из отрезка [1; 1000], для которых сумма цифр значения F(n) равна 27.

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n > 30:
        return n * n + 5 * n + 4
    if n <= 30 and n % 2 == 0:
        return F(n+1) + 3 * F(n+4)
    if n <= 30 and n % 2 != 0:
        return 2 * F(n+2) + F(n+5)

cnt = 0
for n in range(1, 1001):
    if sum(map(int, str(F(n)))) == 27:
        cnt += 1
print(cnt)