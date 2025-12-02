<img width="965" height="174" alt="Задание B(консоль)" src="https://github.com/user-attachments/assets/846ee38e-36b6-4251-875a-74e3700a42a7" /># python_labs

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


# Лабораторная работа №3 по Python

## Задание A — src/lib/text.py

## 1. код normalize:
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError
    if not text:
        return ""
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = text.strip()
    return text

```

## 2. код tokenize:
```python
def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError
    if not text:
        return []
    word_pattern = r"\w+(?:-\w+)*"
    return re.findall(word_pattern, text)

```

## 3. код count_freq:
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, list):
        raise TypeError
    for token in tokens:
        if not isinstance(token, str):
            raise TypeError
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1

    return freq_dict
```

## 4. код top_n:
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise TypeError
    for key in freq:
        if not isinstance(key, str):
            raise TypeError
        if not isinstance(freq[key], int):
            raise TypeError
    sorted_dict = sorted(freq.items(), key = lambda item: (-item[1], item[0]))
    return sorted_dict[:n]

```
## Программа тестирования (text_stats.py):
```python
#тесты normalize
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

#тесты tokenize
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

#тесты count_freq + top_n
tokens_1 = ["a","b","a","c","b","a"]
freq_1 = count_freq(tokens_1)
print(freq_1, top_n(freq_1, 2))
tokens_2 = ["bb","aa","bb","aa","cc"]
freq_2 = count_freq(tokens_2)
print(count_freq(tokens_2))
print(freq_2, top_n(freq_2, 2))
```
## Результат:

![Задание A](https://github.com/user-attachments/assets/b144fad0-3caf-4a8f-92a4-d7ee473567b8)

## Задание B — src/text_stats.py

## код:
```python
text = input("Введите строку:")
tokens = tokenize(text)
freq_dict = count_freq(tokens)
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq_dict)}")
print("Топ-5:")
top_5 = top_n(freq_dict)
for pair in top_5:
    print(f"{pair[0]}:{pair[1]}")
```
## тест:

<img width="454" height="171" alt="Задание B" src="https://github.com/user-attachments/assets/3b174d5d-7b11-45bb-b5a8-8b7f9d3f0c96" />

# Лабораторная работа №4 по Python

## Задание A - src/lab04/io_txt_csv.py

## №1 код read_text:
```python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:


    p = Path(path)
    return p.read_text(encoding=encoding)
```

## №2 код write_csv:
```python
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:

    rows_list = list(rows)
    if rows_list:
        expected = len(rows_list[0])
        for r in rows_list:
            if len(r) != expected:
                raise ValueError("Все строки CSV должны иметь одинаковую длину")

    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)
```

## Задание B - src/lab04/text_report.py

## Дополнительные функции для обработки текста:

```python
def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
```
## №2 основной код в src/lab04/text_report.py:

```python

if __name__ == "__main__":
    from collections import Counter
    from pathlib import Path
    import sys
    from src.lib.text import normalize, tokenize, top_n
    BASE = Path(__file__).resolve().parents[2]
    from src.lab04.io_txt_csv import read_text, write_csv, frequencies_from_text,sorted_word_counts


    INPUT = BASE / "data" / "lab04" / "input.txt"
    OUTPUT = BASE / "data" / "lab04" / "report.csv"
    
    text = read_text(INPUT, "utf-8")


    normalized = normalize(text)
    tokens = tokenize(normalized)

    freq = Counter(tokens)

    sorted_rows = sorted_word_counts(frequencies_from_text(text))

    write_csv(sorted_rows, OUTPUT, header=("word", "count"))

    print("Готово. Отчёт сохранён в:", OUTPUT)
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(frequencies_from_text(text))}")
    if len(sorted_rows) != 0:
        print("Топ-5:")
    for i in range (min(5, len(sorted_rows))):
        print(f"{sorted_rows[i][0]}:{sorted_rows[i][1]}")
```

## Тесты:

## A (Обычный файл):

## Входные данные:
<img width="455" height="317" alt="Задание A(входные данные)" src="https://github.com/user-attachments/assets/b4ae112b-57da-47f8-9e20-fc5d00bf5233" />


## Результат:
<img width="401" height="189" alt="Задание A(результат)" src="https://github.com/user-attachments/assets/36c8588a-e7a0-4a79-8f8c-2131373ed43f" />

## B (Пустой файл):

## Результат:
<img width="609" height="196" alt="Задание B(результат)" src="https://github.com/user-attachments/assets/0da6f54d-2672-4f4d-99cb-34cb273a6e00" />

## Консоль:
<img width="965" height="174" alt="Задание B(консоль)" src="https://github.com/user-attachments/assets/ba1be983-b2b5-4379-91f3-538368c41cc4" />

## C (Кодировка cp1251):

## Входные данные:
<img width="465" height="294" alt="Задание C(входные данные)" src="https://github.com/user-attachments/assets/59dc6dd4-ce1b-47bd-903a-74953525c3b3" />

## Результат:
<img width="669" height="293" alt="Задание C(результат)" src="https://github.com/user-attachments/assets/20a0248e-8b66-4280-b2ab-20594835ee33" />



