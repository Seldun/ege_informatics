'''
5.	Алгоритм вычисления функции F(n) задан следующими соотношениями:
		F(n) =  n · n · n + n при n > 20
		F(n) = 3 · F(n+1) + F(n+3), при чётных n  20
		F(n) = F(n+2) + 2 · F(n+3), при нечётных n  20
Определите количество натуральных значений n из отрезка [1; 1000], при которых значение F(n) не содержит цифру 1.

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n > 20:
        return n * n * n + n
    if n <= 20 and n % 2 == 0:
        return 3 * F(n+1) + F(n+3)
    if n <= 20 and n % 2 != 0:
        return F(n+2) + 2 * F(n+3)

cnt = 0
for n in range(1, 1001):
    if '1' not in str(F(n)):
        cnt += 1
print(cnt)