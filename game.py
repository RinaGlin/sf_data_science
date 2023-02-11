"""The game Guess the number"""

import numpy as np

number = np.random.randint(1, 101) #загадывем число

count = 0                         #количество попыток

while True:
    count +=1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if number > predict_number:
        print ('больше')
    elif number < predict_number:
        print('меньше')
    else:
        print(f'Yooooou did guess this number by {count} attempt')
        break