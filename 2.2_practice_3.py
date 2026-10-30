# Заглавные буквы
print("Заглавные буквы")

s = input()

if " " in s and "  " not in s:
    x = s.find(" ")  # x - индекс пробела
    if s[0] == s[0].upper() and s[x + 1] == s[x + 1].upper():
        print("YES")
    else:
        print("NO")
else:
    print("Между именем и фамилией нету пробела или стоит несколько пробелов!")

# Заглавные буквы
print("Заглавные буквы")

s = input()
print(s.swapcase())


# Хороший оттенок
print("Хороший оттенок")

s = input()
x = "хорош"

if x in s.lower():
    print("YES")
else:
    print("NO")


# Нижний регистр
print("Нижний регистр")

s = input()
x = 0

for i in range(len(s)):
    if (
        s[i] == s[i].lower()
        and s[i].lower()
        in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    ):
        x += 1
print(x)
