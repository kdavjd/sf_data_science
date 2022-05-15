"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

def predict_by_divide(number: int =1, min_number: int=1, max_number: int=100) -> int:
    """Функция делит исследуемую область на равные интервалы в две единицы, отбрасывая 
    хвосты. 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        min_number (int, optional): Нижняя граница числа. Defaults to 1.
        max_number (int, optional): Верхняя граница числа. Defaults to 100.

    Returns:
        int: Число попыток.
    """
    count=0
    
    divide_list = [border for border in range(min_number,max_number) if \
        border%2 == 0]
    
    if min(divide_list) < number < max(divide_list): #Начало и конец строго отбрасываются.
        for border in divide_list:
            if border > number: #Поскольку шаг два, то число либо предыдущее, либо то что за ним.
                if number == border-2:
                    count += 1
                    break                                   
                elif number == border-1:
                        count+=1
                        break
                else:
                    raise Exception('Поздравляю, что-то не так.')
            
            
    elif max_number >= number >= max(divide_list): #Ищем число в верхнем хвосте
        if number == max(divide_list)+2:
            count += 1           
        elif number == max(divide_list)+1:
            count += 1
        elif number == max(divide_list):
            count += 1       
        else:
            raise Exception('Ошибка в верхних граничных исключениях')
    
    elif min_number <= number <= min(divide_list): #Ищем число в нижнем хвосте
        if number == min(divide_list)-2:
            count += 1                
        elif number == min(divide_list)-1:
            count += 1
        elif number == min(divide_list):
            count += 1
        else:
            raise Exception('Ошибка в нижних граничных исключениях')
        
    
    return count
 
        
if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(predict_by_divide)
    
    
