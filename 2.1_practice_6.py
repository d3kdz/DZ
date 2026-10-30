# Таблица-1
print("Таблица-1")
n = int(input())

if 1 <= n <= 9:

    for i in range(n):
        for j in range(3):
            print(n, end=" ")
        print()

else:
    print("Не соответствует условию - 1 <= n <= 9")


# Таблица-2
print("Таблица-2")
n = int(input())

if 1 <= n <= 9:

    for i in range(n):
        for j in range(5):
            print(i + 1, end=" ")
        print()

else:
    print("Не соответствует условию - 1 <= n <= 9")


# Таблица-3
print("Таблица-3")
n = int(input())
x = 1

if 1 <= n <= 9:

    for i in range(n):
        for j in range(1, 10):
            print(x, "+", j, "=", x + j)
        print()
        x += 1

else:
    print("Не соответствует условию - 1 <= n <= 9")


# Численный треугольник 1
print("Численный треугольник 1")
n = int(input())

if n > 0:

    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end="")
        print()

else:
    print(n, "- не натуральное число!")


# Звёздный треугольник
print("Звёздный треугольник")
n = int(input())
s = "*"
cnt = 0

if n > 0 and n % 2 != 0:

    for i in range(n):
        for j in range(i + 1):
            print(s, end="")
        cnt += 1
        print()
        if j + 1 == (n + 1) / 2:
            break

    for c in range(cnt):
        cnt -= 1
        print(cnt * s)

else:
    print(n, "- не натуральное или четное число!")


# Делители-1
print("Делители-1")
n = int(input())
p = "+"
c = 0

if n > 0:
    for i in range(n):
        print(i + 1, end="")
        for j in range(i + 1):
            c += 1
            if (i + 1) % c == 0:
                print(p, end="")
        c = 0
        print()

else:
    print(n, "- не натуральное число!")


# Численный треугольник 2
print("Численный треугольник 2")
n = int(input())
cnt = 0

if n > 0:

    for i in range(n):
        for j in range(i + 1):
            cnt += 1
            print(cnt, end=" ")
        print()

else:
    print(n, "- не натуральное число!")


# Подставь и узнаешь
print("Подставь и узнаешь")
n = int(input())
m = int(input())
found = False

for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a + 3 * b + 2 * c == m:
                print(a, "+ 3 x", b, "+ 2 x", c, "=", m)
                found = True

if not found:
    print("При заданных n и m решений не существует.")
