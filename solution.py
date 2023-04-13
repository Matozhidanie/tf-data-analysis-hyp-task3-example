import pandas as pd
import numpy as np
from scipy import stats

chat_id = 481557740 # Ваш chat ID, не меняйте название переменной

def solution(hist: np.array, new: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия

    # уровень значимости
    uroven = 0.06

    # при гипотезе принимаем p = p0 (роста при новом способе нет)
    # тестируем отклонение вверх (есть ли рост?) - альтернатива правосторонняя

    # гипотеза p<=p0
    # альтернатива p>p0

    # вычисления p-value етодом T-test 
    result = stats.ttest_ind (a=hist, b=new, equal_var=False, alternative='less')

    print(result.statistic)
    print(result.pvalue)

    if (result.pvalue < uroven) and (result.statistic < 0):
        otvet = bool(1)
    else:
        otvet = bool(0)

    return otvet # Ваш ответ, True или False
