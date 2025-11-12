'''18.	Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n, если n ≥ 10 000,
F(n) = F(n + 2) – 3, если n < 10 000 и n чётное,
F(n) = F(n + 2) + 1 , если n < 10 000 и n нечётное.
Чему равно значение выражения F(9994) – F(9980)?
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 2 == 0:
        return F(n + 2) - 3
    return F(n + 2) + 1

print(F(9994) - F(9980))