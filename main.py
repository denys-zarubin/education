a = float(input("Введите число:"))
print("Выбирите функцию: +, -, /, *, ^")
b = input(":")
if b == "-":
    c = float(input("Введите 2ое число:"))
    result = a - c
    print("Ответ:",result)
if b == "+":
    c = float(input("Введите 2ое число:"))
    result = a + c
    print("Ответ:",result)
if b == "/":
    c = float(input("Введите 2ое число:"))
    result = a / c
    print("Ответ:",result)
if b == "*":
    c = float(input("Введите 2ое число:"))
    result = a * c
    print("Ответ:",result)
if b == "^":
    c = float(input("Введите степень в которую хотите возвести число:"))
    result = a**c
    print("Ответ:",result)
else: print("Ошибка, такой функции нет.")


