'''20.	Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n = 1
F(n) = (2n – 1) · F(n – 1), если n > 1.
Чему равно значение выражения F(3516) / F(3513)?
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n == 1:
        return 1
    return (2 * n - 1) * F(n - 1)

print(F(3516) / F(3513))