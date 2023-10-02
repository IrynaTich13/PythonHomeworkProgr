#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть


n = int(input('Введите число монеток: '))
from random import randint

countTails = 0
countArms = 0

for i in range(n):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0:
        countTails += 1
    else:
        countArms += 1
print(f'Необходимо перевернуть {min(countTails, countArms)} монет')