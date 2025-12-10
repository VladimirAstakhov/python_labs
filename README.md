
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
# Ввод текста происходит до 
## код:
```python
print("Введите текст:")
text = str(sys.stdin.readlines())
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
## Путь к файлу задается по схеме: обращаемся к текущему файлу -> поднимаемся в родительскую директорию (python_labs) -> спускаемся до файлов, в которые загружаем input и output. 
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

##Если не существует файла по указанному пути, всплывает ошибка:
<img width="1343" height="60" alt="файл не существует" src="https://github.com/user-attachments/assets/301baa75-033d-4e80-996f-65db5e2ab9c6" />



## A (Обычный файл):

## Входные данные:
<img width="455" height="317" alt="Задание A(входные данные)" src="https://github.com/user-attachments/assets/b4ae112b-57da-47f8-9e20-fc5d00bf5233" />


## Результат:
<img width="401" height="189" alt="Задание A(результат)" src="https://github.com/user-attachments/assets/36c8588a-e7a0-4a79-8f8c-2131373ed43f" />

## B (Пустой файл), выводится:
## B (Пустой файл), word,count:
## Результат:
<img width="609" height="196" alt="Задание B(результат)" src="https://github.com/user-attachments/assets/0da6f54d-2672-4f4d-99cb-34cb273a6e00" />

## Консоль:
<img width="965" height="174" alt="Задание B(консоль)" src="https://github.com/user-attachments/assets/ba1be983-b2b5-4379-91f3-538368c41cc4" />

## C (Кодировка cp1251):

## Входные данные:
<img width="465" height="294" alt="Задание C(входные данные)" src="https://github.com/user-attachments/assets/59dc6dd4-ce1b-47bd-903a-74953525c3b3" />

## Результат:
<img width="669" height="293" alt="Задание C(результат)" src="https://github.com/user-attachments/assets/20a0248e-8b66-4280-b2ab-20594835ee33" />


# Лабораторная работа №5 по Python

## Задание A — JSON ↔ CSV

## функция json_to_csv

```
Преобразует JSON-файл в CSV.
Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
Кодировка UTF-8. Порядок колонок — как в первом объекте.
```
```python

def json_to_csv(json_path, csv_path):
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if json_path.suffix.lower() != ".json":
        raise ValueError("Неверный тип входного файла: нужен .json")

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Неверный тип выходного файла: нужен .csv")

    if not json_path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать список объектов")

    fieldnames = list(data[0].keys())
    for item in data:
        row = {key: item.get(key, "") for key in fieldnames}
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
```

## функция csv_to_json

```
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    
```
```python
def csv_to_json(csv_path, json_path):
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Ожидается CSV-файл на входе")
    if json_path.suffix.lower() != ".json":
        raise ValueError("Ожидается JSON-файл на выходе")

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV пустой или без заголовка")

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```

## Задание B —  CSV → XLSX

```
    используется openpyxl
    Конвертирует CSV в XLSX.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    
```

```python
def csv_to_xlsx(csv_path, xlsx_path):
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.suffix.lower() != ".csv":
        raise ValueError("Ожидается CSV-файл на входе")
    if xlsx_path.suffix.lower() != ".xlsx":
        raise ValueError("Ожидается XLSX-файл на выходе")

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    widths = {}

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            ws.append(row)

            for i, cell in enumerate(row):
                length = len(str(cell))
                widths[i] = max(widths.get(i, 8), length)

    for i, w in widths.items():
        col_letter = ws.cell(row=1, column=i+1).column_letter
        ws.column_dimensions[col_letter].width = w + 2

    wb.save(xlsx_path)
```
## Тесты (из data/samples)

#Файл запускающий тестирование:

```python
if __name__ == "__main__":
    from src.lab05.csv_xlsx import csv_to_xlsx
    from src.lab05.json_csv import json_to_csv, csv_to_json
    from pathlib import Path

    BASE = Path(__file__).resolve().parents[2]

    INPUT_JSON = BASE / "data" / "samples" / "people.json"
    OUTPUT_CSV = BASE / "data" / "out" / "people_from_json.csv"

    INPUT_CSV = BASE / "data"  / "samples" / "people.csv"
    OUTPUT_JSON = BASE / "data"  / "out" / "people_from_csv.json"

    INPUT_CSV_2 = BASE / "data"  / "samples" / "cities.csv"
    OUTPUT_XLSX = BASE / "data"  / "out" / "people.xlsx"

    json_to_csv(INPUT_JSON, OUTPUT_CSV)
    csv_to_json(INPUT_CSV, OUTPUT_JSON)
    csv_to_xlsx(INPUT_CSV_2, OUTPUT_XLSX)
```

## конвертация json в csv:
<img width="366" height="223" alt="image" src="https://github.com/user-attachments/assets/1dc2c765-53cd-4280-adb1-c67b5305c571" />

## конвертация csv в json:
<img width="507" height="819" alt="image" src="https://github.com/user-attachments/assets/c3f79b73-b0e2-4d16-a5de-a022430c3251" />

## конвертация csv в xlsx:
<img width="445" height="267" alt="image" src="https://github.com/user-attachments/assets/945e1d02-184e-46b6-83fe-ae8be769b790" />


# Лабораторная работа №6 по Python

## команда cat

```
Осуществляет построчный вывод файла
Подкоманда/ флаг -n - означает построчный, пронумерованный вывод строк

```
## тесты:

## help
<img width="931" height="263" alt="cat_help" src="https://github.com/user-attachments/assets/f2a2c992-dadc-452f-bae7-6c407c72db00" />

## работа команды с people.csv из data/samples
<img width="1196" height="234" alt="cat_csv" src="https://github.com/user-attachments/assets/b36a2674-053c-46f8-b4c1-2f1b95376859" />
<img width="1304" height="236" alt="cat_csv_-n" src="https://github.com/user-attachments/assets/136e276b-366c-4133-903e-5459b6b49958" />

## команда stats

```
Анализирует частоту слов в текстовом файле и выводит топ-N наиболее часто встречающихся слов
Аргумент --top N - определяет количество выводимых слов (по умолчанию 5)

```
## тесты:

## help
<img width="953" height="260" alt="stats_help" src="https://github.com/user-attachments/assets/2907c55d-dca2-4c0e-85e3-24d01327244d" />

## работа команды с people.csv из data/samples (для args.top = 5 - значение по умолчанию и args.top = 3)

<img width="1187" height="212" alt="stats_csv" src="https://github.com/user-attachments/assets/5b4b09eb-dc8f-4b81-9db9-d56b79e4b941" />
<img width="1372" height="145" alt="stats_csv_top3" src="https://github.com/user-attachments/assets/9d15d0cb-a21b-4fb5-8584-908d94b9fa97" />

## команды конвертирующие файлы json2csv, csv2json, csv2xlsx
## json2csv
```
Конвертирует данные из формата JSON в формат CSV
Аргументы: --in (входной JSON файл), --out (выходной CSV файл)

```
## команда csv2json

```
Конвертирует данные из формата CSV в формат JSON
Аргументы: --in (входной CSV файл), --out (выходной JSON файл)

```
## команда csv2xlsx

```
Конвертирует данные из формата CSV в формат XLSX (Excel)
Аргументы: --in (входной CSV файл), --out (выходной XLSX файл)
Автоматически настраивает ширину столбцов по содержимому
```
## help
<img width="663" height="770" alt="people_from_csv_to_json" src="https://github.com/user-attachments/assets/4dd5aef4-dac5-4cd6-9cd3-87c3f39166b1" />

<img width="825" height="326" alt="people_from_json_to_csv" src="https://github.com/user-attachments/assets/2ec4f06f-ff86-43bf-b40e-72ef1f305ed9" />

<img width="333" height="151" alt="people_xlsx" src="https://github.com/user-attachments/assets/40201e02-f681-440c-adea-4a9c5e564b45" />

## Тесты этих подкоманд дают аналогичные результаты что и в лабораторной 5, команды:
```
JSON → CSV
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv

CSV → JSON
python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json

CSV → XLSX
python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```
## общие help, для cli_convert и cli_text

```
python -m src.lab06.cli_text --help
```
<img width="979" height="455" alt="image" src="https://github.com/user-attachments/assets/3947ae5a-68b9-4be7-9e8b-d4a5a3a9a096" />

```
python -m src.lab06.cli_convert --help
```

<img width="1061" height="397" alt="image" src="https://github.com/user-attachments/assets/44079af8-bc33-4ad6-8f1a-a36000d169d2" />

