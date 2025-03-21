import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток N
    """

    count = 0  # устанавливаем счётчик попыток в 0
    # приравниваем текущие верхние и нижние границы к заданным для случайного числа
    low_num = low_border
    high_num = high_border

    while True:
        count += 1
        predict_number = np.random.randint(low_num, high_num)  # предполагаемое число
        # если загаданное число меньше предполагаемого, устанавливаем верхнюю границу
        # равную предполагаемому
        if number < predict_number:
            high_num = predict_number
        # если загаданное число больше предполагаемого, устанавливаем нижнюю границу
        # равную предполагаемому
        elif number > predict_number:
            low_num = predict_number
        else:
            number == predict_number
            break  # выход из цикла, если угадали
    return count


low_border, high_border = 1, 101  # Задаём границы для случайного числа


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        low_border, high_border, size=(1000)
    )  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток
    score_min = int(np.min(count_ls))  # находим минимальное количество попыток
    score_max = int(np.max(count_ls))  # находим минимальное количество попыток

    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    print(f"Ваш алгоритм угадывает число в минимум за: {score_min} попыток")
    print(f"Ваш алгоритм угадывает число в максимум за: {score_max} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
