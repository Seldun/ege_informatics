'''8.	Алгоритмы вычисления функций F(n) и G(n) где n – целое число, заданы следующими соотношениями (// обозначает деление нацело):
F(n) = n, при n < 50,
F(n) = 2 G(50 – n // 2), при n > 49,
G(n) = 10, при n > 40,
G(n) = 30 + F(n + 600 // n), при n < 41
Чему равно значение F(80)?
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n < 50:
        return n
    return 2 * G(50 - n // 2)

@lru_cache(maxsize=None)
def G(n):
    if n > 40:
        return 10
    return 30 + F(n + 600 // n)

print(F(80))