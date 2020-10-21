n = int(input("Введите число, до которого "))
res = []
for i in range(2, n + 1):
    is_simple = True
    for j in range(2, int(pow(i, 1/2)) + 1):
        if i % j == 0:
            is_simple = False
    mirror = int(''.join(reversed(str(i))))
    for j in range(2, int(pow(mirror, 1/2)) + 1):
        if mirror % j == 0:
            is_simple = False
    if is_simple:
        res.append(i)

print(res)



