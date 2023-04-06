import pandas as pd
import numpy as np


chat_id = 38897891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    def MyLogN_Moment_Method(X):
        a_est = np.mean(np.log(X - 59))
        sigma_est = np.sqrt(np.mean((np.log(X - 59)-a_est)**2))
        return a_est, sigma_est
    
    a_est, sigma_est = MyLogN_Moment_Method(x)
    
    return a_est # Ваш ответ
