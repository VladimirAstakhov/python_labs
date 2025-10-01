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

