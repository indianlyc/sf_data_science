"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np



def random_predict(number: int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break

    return count


def binary_search(number: int=1) -> int:
    """Реализуем бинарный поиск для угадывания числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_n = 100
    min_n = 1
    while True:
        count += 1
        predict_number = (max_n + min_n) // 2
        if predict_number < number:
            min_n = predict_number+1
        elif predict_number > number:
            max_n = predict_number-1
        if predict_number == number:
            break

    return count


def score_game(func_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш подход

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(func_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    score_game(binary_search)
