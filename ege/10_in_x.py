def to_base(n, base):
    s = ''
    while n > 0:
        n, r = divmod(n, base)
        s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[r] + s
    return s or '0'



print(to_base(42, 13))   # → "33"
print(to_base(255, 16))  # → "FF"
print(to_base(0, 12))    # → "0"

# библиотека для алфавита       from string import printable