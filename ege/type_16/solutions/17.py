'''
17.	Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n, если n ≥ 10 000,
F(n) = n/4 + F(n / 4 + 2), если n < 10 000 и n делится на 4,
F(n) = 1 + F(n + 2) , если n < 10 000 и n не делится на 4.
Чему равно значение выражения F(174) – F(3)?

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 4 == 0:
        return n / 4 + F(n / 4 + 2)
    return 1 + F(n + 2)

print(F(174) - F(3))