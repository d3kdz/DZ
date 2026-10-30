# Плохие комментарии
print("Плохие комментарии")

n = int(input())
x = 0
for i in range(n):
    s = input()
    if s.isspace() or s == "":
        print(i + 1, ": COMMENT SHOULD BE DELETED")
    else:
        print(i + 1, s)


# Проверь никнейм
print("Проверь никнейм")

s = input()

if s[0] == "@" and 5 <= len(s) <= 15 and s[1:].isalnum():
    print("Correct")
else:
    print("Incorrect")


# Автомобильный номер
print("Автомобильный номер")

s = input()
a = "АВЕКМНОРСТУХ"
if (
    s[0] in a
    and s[4] in a
    and s[5] in a
    and s[1:4].isdigit()
    and s[7:10].isdigit()
    and 2 <= len(s[7:]) <= 3
    and s[6] == "_"
):
    print("YES")
else:
    print("NO")
