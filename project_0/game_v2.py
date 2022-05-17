"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from itertools import count
import numpy as np

count

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

def predict_by_divide(number: int =1, min_number: int=1, max_number: int=100, count: int=0) -> int:
    """Функция делит исследуемую область на равные интервалы в две единицы, отбрасывая 
    хвосты. Это не самая красивая или эффективная функция, но первая рабочая, написанная мной. 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        min_number (int, optional): Нижняя граница числа. Defaults to 1.
        max_number (int, optional): Верхняя граница числа. Defaults to 100.
        count (int, optional): Число попыток. Defaults to 0.

    Returns:
        int: Число попыток.
    """
    
    
    divide_list = [border for border in range(min_number,max_number) if \
        border%2 == 0]
    
    if min(divide_list) < number < max(divide_list): #Начало и конец строго отбрасываются.
        for border in divide_list:
            count += 1
            if border > number: #Поскольку шаг два, то число либо предыдущее, либо то что за ним.
                if number == border-1:
                    count += 1
                    break                                   
                elif number == border-2:
                    count += 2
                    break
                else:
                    raise Exception('Ошибка в исследуемом диапазоне')
            
            
    elif max_number >= number >= max(divide_list): #Ищем число в верхнем хвосте
        count += 1 #+1 потому что до этого места мы искали в главном интервале
        if number == max(divide_list):
            count += 1           
        elif number == max(divide_list)+1:
            count += 2
        elif number == max(divide_list)+2:
            count += 3       
        else:
            raise Exception('Ошибка в верхних граничных исключениях')
    
    elif min_number <= number <= min(divide_list): #Ищем число в нижнем хвосте
        count += 2 #+2 потому что до этого места мы искали в главном интервале и в конце
        if number == min(divide_list):
            count += 1                
        elif number == min(divide_list)-1:
            count += 2
        elif number == min(divide_list)-2:
            count += 3
        else:
            raise Exception('Ошибка в нижних граничных исключениях')
        
    
    return count
 

def predict_by_recursion(number, min_number: int=1, max_number: int=100) -> predict_by_divide():
    
    """Функция сужает исследуемую область для функции predict_by_divide()

    Args:
        number (int, optional): _description_. Defaults to 1.
        min_number (int, optional): _description_. Defaults to 1.
        max_number (int, optional): _description_. Defaults to 100.

    Returns:
        int: predict_by_divide()
    """
    max_number
    min_number
    count = 0
    
    def max_border_near(number: int):  
        nonlocal count
        nonlocal max_number
        average = int(np.average([min_number,max_number]))
        if number < average:
            if max_number - average < min_number:
                return max_number
            max_number -= average
            count += 1
            return max_border_near(number)
        return max_number
    
    def min_border_near(number: int):
        nonlocal count
        nonlocal min_number
        average = (int(np.average([min_number,max_number])))
        if number > average:
            if count > 10: 
                #В приложенном файле прзентации для юпитера я попытался показать
                #почему тут такое число, но не справился. Нашел его руками.               
                return min_number
            
            next_step = (average + min_number)/2
            if  next_step > max_number:
                return min_number
            min_number = next_step
            count += 1
            return min_border_near(number)
        
        return min_number
       
    
    if number < int(np.average([min_number,max_number])):
        if number == min_number: #Исключение, которое не нашел как элегантно обойти.
            count += 1
            return count
        count += 1 #+1 потому что до этого места мы сравнивали с минимумом
        max_border_near(number)
        min_border_near(number)
    else:
        count += 1
        min_border_near(number)
        max_border_near(number)
    return predict_by_divide(number, int(min_number), int(max_number), count)
        

    
if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(predict_by_divide)
    score_game(predict_by_recursion)
    
    
