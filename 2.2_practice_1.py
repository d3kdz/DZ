# В столбик 1
print("В столбик 1")
s = input()
x = 0

for i in range(len(s)):
    if x % 2 == 0:
        print(s[x])
    x += 1


# В столбик 2
print("В столбик 2")
s = input()
x = 0

for i in range(len(s)):
    x -= 1
    print(s[x])


# ФИО
print("ФИО")
i = input()
f = input()
o = input()
print(f[0], i[0], o[0])


# Цифра 1
print("Цифра 1")
n = input()
x = 0

for i in range(len(n)):
    x += int(n[i])
print(x)


# Цифра 2
print("Цифра 2")
s = input()

for i in range(len(s)):
    if s[i] in "0123456789":
        print("Цифра")
        break

else:
    print("Цифр нет")


# Сколько раз?
print("Сколько раз?")
s = input()
x = 0
y = 0

for i in range(len(s)):
    if s[i] == "+":
        x += 1
    if s[i] == "*":
        y += 1

print("Символ + встречается", x, "раз(а)")
print("Символ * встречается", y, "раз(а)")


# Одинаковые соседи
print("Одинаковые соседи")
s = input()
x = 0

for i in range(len(s)):
    if s[i] == s[i - 1]:
        x += 1
print(x)


# Гласные и согласные
print("Гласные и согласные")
s = input()
a = 0  # Счетчик гласных
b = 0  # Счетчик согласных

for i in range(len(s)):
    if s[i] in "ауоыиэяюеАУОЫИЭЯЮЕ":
        a += 1
    if s[i] in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
        b += 1

print("Количество гласных букв равно", a)
print("Количество согласных букв равно", b)
