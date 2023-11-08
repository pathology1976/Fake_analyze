# Скрипт создает датафрейм. В него надо ввести количество колонок, название для каждой колонки
# и размах для рандома. Датафрейм заполнит 60 значений.

import pandas as pd
import numpy as np

num_columns = int(input("количество колонок: "))
column_ranges = []

for i in range(num_columns):
    col_name = input(f" имя для колонки {i+1}: ")
    min_val = float(input(f"минимальное значение {col_name}: "))
    max_val = float(input(f"максимальное значение {col_name}: "))
    column_ranges.append((col_name, min_val, max_val))

df = pd.DataFrame()

for col_name, min_val, max_val in column_ranges:
    random_values = np.random.uniform(min_val, max_val, 60)
    df[col_name] = random_values

# По желанию сформированный датафрейм можно сохранить через пандас, раскоментиров код ниже, но функцию принт
# тогда лучше закоментировать

#file_path = "ты_пидор.csv"
#df.to_csv(file_path, index=False) 

print(df)