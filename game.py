""" Игра Угадай число"""

import numpy as np
number = np.random.randint(1, 101)

count = 0
while True:
    count += 1
    predict_number = int(input("Введите число от 1 до 100: "))
    
    if predict_number > number:
        print ("Ваше число больше загаданного")
    elif predict_number < number:
        print ("Ваше число меньше загаданного")
    else:
        print (f"Вы угадали это число - {number} за {count} попыток")
        break
    
               
        