#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите максимальное число:"))
i = 1
while i<=number:
    print(i)
    i *= 2