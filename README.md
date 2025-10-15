# python_labs

# Лабораторная работа №1 по Python

## Задание 1 — Привет и возраст
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![image_01](https://github.com/user-attachments/assets/73fe6699-ecbf-45cb-b0ff-d8c60a980e57)


## Задание 2 — Сумма и среднее
```python
a = float(input("a: "))
b = float(input("b: "))
print(f"sum={a+b:.2f}; avg={(a+b)/2:.2f}")
```
![image_02](https://github.com/user-attachments/assets/b5ea40ab-52f3-4c50-b49e-ef12eb72cd2c)


## Задание 3 — Чек: скидка и НДС
```python
price = float(input("Цена (₽): "))
discount = float(input("Скидка (%): "))
vat = float(input("НДС (%): "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
![image_03](https://github.com/user-attachments/assets/df98d635-c647-4125-9dd7-43f879db0b58)


## Задание 4 — Минуты → ЧЧ:ММ
```python
m = int(input())
print(f"{m//60}:{m%60:02d}")
```
![image_04](https://github.com/user-attachments/assets/50b8811d-5d3a-4c75-a20f-6c2fd0c58581)


## Задание 5 — Инициалы и длина строки
```python
full_name = input("ФИО: ")
counter = 0
i = 0
print('Инициалы: ', end='')
while (i < len(full_name)):
    while (i < len(full_name) and full_name[i] == ' '):
        i += 1
    if (i < len(full_name)):
        print(full_name[i], end='')
        while (i < len(full_name) and full_name[i] != ' '):
            i += 1
            counter += 1
    i += 1
print('.')
print(f"Длина (символов): {counter + 2}")



```
![image_05](https://github.com/user-attachments/assets/f448437d-c7fa-422a-b74a-d17b986a48b0)




# Лабораторная работа №2 по Python

## Задание 1 — arrays.py
```python
def min_max(nums: list[float | int]):
    if (len(nums) == 0):
        return "ValueError"
    return (max(nums), min(nums))
def unique_sorted(nums: list[float | int]):
    return list(set(nums))
def flatten(mat: list[list | tuple]):
    for each_list in mat:
        if (not isinstance(each_list, list)) and (not isinstance(each_list, tuple)):
            return "ValueError"

    return [element for each_list in mat for element in each_list]
```
## Тесты:
```python
print("min_max tests")
test_min_max_1 = [3, -1, 5, 5, 0]
test_min_max_2 = [42]
test_min_max_3 = [-5, -2, -9]
test_min_max_4 = []
print(min_max(test_min_max_1))
print(min_max(test_min_max_2))
print(min_max(test_min_max_3))
print(min_max(test_min_max_4))
print()

print("unique_sorted tests")
test_unique_sorted_1 = [3, 1, 2, 1, 3]
test_unique_sorted_2 = []
test_unique_sorted_3 = [-1, -1, 0, 2, 2]
test_unique_sorted_4 = [1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(test_unique_sorted_1))
print(unique_sorted(test_unique_sorted_2))
print(unique_sorted(test_unique_sorted_3))
print(unique_sorted(test_unique_sorted_4))
print()

print("flatten tests")
test_flatten_1 = [[1, 2], [3, 4]]
test_flatten_2 = [[1, 2], (3, 4, 5)]
test_flatten_3 = [[1], [], [2, 3]]
test_flatten_4 = [[1, 2], "ab"]
print(flatten(test_flatten_1))
print(flatten(test_flatten_2))
print(flatten(test_flatten_3))
print(flatten(test_flatten_4))
```

<img width="688" height="563" alt="image_01" src="https://github.com/user-attachments/assets/99a79a69-26e5-404d-b523-79518f063086" />

## Задание 2 — matrix.py
```python
def is_rectangular(mat: list[list[float | int]]):
    if (len(mat) == 0):
        return -1
    row_size = len(mat[0])
    for row in mat:
        if (len(row) != row_size):
            return 0
    return 1


def transpose(mat: list[list[float | int]]):
    if (is_rectangular(mat) == -1):
        return mat
    if (is_rectangular(mat) == 0):
        return "ValueError"
    row_size = len(mat[0])
    column_size = len(mat)
    mat_transpose = [0] * row_size
    for i in range(0, row_size):
        row = [0] * column_size
        for j in range(0,column_size):
            row[j] = mat[j][i]
        mat_transpose[i] =  row
    return mat_transpose

def row_sums(mat: list[list[float | int]]):
    if (is_rectangular(mat) == -1):
        return mat
    if (is_rectangular(mat) == 0):
        return "ValueError"
    sums = []
    for row in mat:
        sum_in_row = 0
        for element in row:
            sum_in_row += element
        sums.append(sum_in_row)
    return sums
def col_sums(mat: list[list[float | int]]):
    if (is_rectangular(mat) == -1):
        return mat
    if (is_rectangular(mat) == 0):
        return "ValueError"
    column_size = len(mat)
    row_size = len(mat[0])
    sums = []
    for i in range (0, row_size):
        sum_in_column = 0
        for j in range(0, column_size):
            sum_in_column += mat[j][i]
        sums.append(sum_in_column)
    return sums
```
## Тесты:
```python
print("transpose tests")
test_transpose_1 = [[1, 2, 3]]
test_transpose_2 = [[1], [2], [3]]
test_transpose_3 = [[1, 2], [3, 4]]
test_transpose_4 = []
test_transpose_5 = [[1, 2], [3]]
print(transpose(test_transpose_1))
print(transpose(test_transpose_2))
print(transpose(test_transpose_3))
print(transpose(test_transpose_4))
print(transpose(test_transpose_5))

print("row_sums tests")
test_row_sums_1 = [[1, 2, 3], [4, 5, 6]]
test_row_sums_2 = [[-1, 1], [10, -10]]
test_row_sums_3 = [[0, 0], [0, 0]]
test_row_sums_4 = [[1, 2], [3]]
print(row_sums(test_row_sums_1))
print(row_sums(test_row_sums_2))
print(row_sums(test_row_sums_3))
print(row_sums(test_row_sums_4))

print("col_sums tests")
test_col_sums_1 = [[1, 2, 3], [4, 5, 6]]
test_col_sums_2 = [[-1, 1], [10, -10]]
test_col_sums_3 = [[0, 0], [0, 0]]
test_col_sums_4 = [[1, 2], [3]]
print(col_sums(test_col_sums_1))
print(col_sums(test_col_sums_2))
print(col_sums(test_col_sums_3))
print(col_sums(test_col_sums_4))
```
<img width="523" height="535" alt="image_02" src="https://github.com/user-attachments/assets/7f5d113d-c82f-4283-bd01-bb839261fe1b" />


## Задание 3 — tuples.py
```python
def format_record(rec: tuple[str, str, float]):
    final_form = ""
    name = rec[0].title().split()
    group = rec[1]
    gpa = str(round(rec[2], 2))
    if len(name) == 3:
        final_form = name[0] + " " + name[1][0] + ". " + name[2][0] + "., гр. " + group + ", GPA " + gpa
    elif len(name) == 2:
        final_form = name[0] + " " + name[1][0] + "., гр. " + group + ", GPA " + gpa
    else:
        return "ValueError"
    if (len(gpa.split(".")[1]) == 1):
        final_form += "0"
    return final_form

```
## Тесты:
```python
test_1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
test_2 = ("Петров Пётр", "IKBO-12", 5.0)
test_3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
test_4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(test_1))
print(format_record(test_2))
print(format_record(test_3))
print(format_record(test_4))

```
<img width="456" height="222" alt="image_03" src="https://github.com/user-attachments/assets/d5bbfde2-005a-4346-bc39-9a2101ff7274" />


