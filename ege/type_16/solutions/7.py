'''7.	Алгоритм вычисления функции F(n) задан следующими соотношениями:
		F(n) =  2 · n · n + 4 · n + 3, при n  15
		F(n) = F(n–1) + n · n + 3, при n > 15, кратных 3
		F(n) = F(n–2) + n – 6, при n > 15, не кратных 3
Определите количество натуральных значений n из отрезка [1; 1000], для которых все цифры значения F(n) нечётные.
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    if n > 15 and n % 3 == 0:
        return F(n-1) + n * n + 3
    if n > 15 and n % 3 != 0:
        return F(n-2) + n - 6

cnt = 0
for n in range(1, 1001):
    if all(int(d) % 2 != 0 for d in str(F(n))):
        cnt += 1
print(cnt)