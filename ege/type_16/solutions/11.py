'''11.	Алгоритм вычисления функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:
F(n) = 0 при n = 0
F(n) = F(n/2) – 1 при n > 0 для чётных n
F(n) = 3 + F(n–1) при n > 0 для нечётных n
Сколько различных значений может принимать функция F(n) для чисел n, меньших 1000?

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n // 2) - 1
    if n > 0 and n % 2 != 0:
        return 3 + F(n - 1)

values = set()
for n in range(1000):
    values.add(F(n))
print(len(values))