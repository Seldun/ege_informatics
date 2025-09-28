from string import printable

for x in printable[:29]:
    a = int(f'923{x}874',29) + int(f'524{x}6152', 29)
    if a%28 == 0:
        print(x, a//28)