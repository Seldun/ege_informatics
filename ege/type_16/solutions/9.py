'''9.	Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(1) = 1,
F(n) = F(n / 2) + 1, когда n  2 и чётное,
F(n) = F(n – 1) + n , когда n  2 и нечётное.
Назовите количество значений n на отрезке [1;100000], для которых F(n) равно 16.

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return F(n // 2) + 1
    if n >= 2 and n % 2 != 0:
        return F(n - 1) + n

cnt = 0
for n in range(1, 100001):
    if F(n) == 16:
        cnt += 1
print(cnt)