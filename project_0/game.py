"""Игра угадай число"""
import numpy as np

number:int = np.random.randint(1, 101)

count:int = 0

while True:
    count += 1
    predict_number:int = int(input("Угадай число от 1 до 100: "))

    if predict_number > number:
        print("Число должно быть меньше!")
    elif predict_number < number:
        print("Число должно быть больше!")
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break
