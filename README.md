
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

# Файл запускающий тестирование:

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

# Лабораторная работа №7 по Python

##  Тестирование: pytest + стиль (black)

## Тест normalize

```python
@pytest.mark.parametrize(
    "text, expected",
    [
        ("ПрИвЕт\nМиР\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(text, expected):
    assert normalize(text) == expected
```


## Тест tokenize

```python
@pytest.mark.parametrize(
    "text, expected_tokens",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😃 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("!!! ??? ###", []),
    ],
)
def test_tokenize_basic(text, expected_tokens):
    assert tokenize(text) == expected_tokens
```


## Тест count_freq

```python
@pytest.mark.parametrize(
    "tokens, expected_freq",
    [
        (
            ["a", "b", "a", "c", "b", "a"],
            {"a": 3, "b": 2, "c": 1},
        ),
        (
            ["bb", "aa", "bb", "aa", "cc"],
            {"bb": 2, "aa": 2, "cc": 1},
        ),
        (["a", "a", "a"], {"a": 3}),
        (["b", "a"], {"b": 1, "a": 1}),
    ],
)
def test_count_freq_basic(tokens, expected_freq):
    assert count_freq(tokens) == expected_freq
```


## Тест top_n

```python
@pytest.mark.parametrize(
    "freq, n, expected_top",
    [
        (
            {"a": 3, "b": 2, "c": 1},
            2,
            [("a", 3), ("b", 2)],
        ),
        (
            {"bb": 2, "aa": 2, "cc": 1},
            2,
            [("aa", 2), ("bb", 2)],
        ),
        ({"b": 2, "a": 2, "c": 1}, 2, [("a", 2), ("b", 2)]),
    ],
)
def test_top_n_basic(freq, n, expected_top):
    assert top_n(freq, n) == expected_top
```
## Работа тестов:

<img width="1409" height="825" alt="тесты функций обработки текста" src="https://github.com/user-attachments/assets/de732ff5-8d99-479b-911e-1765e8f5fad0" />


## Тест json_to_csv ( Обычные файлы)

```python
@pytest.mark.parametrize(
    "data",
    [
        [
            {"name": "Alice", "age": 22},
            {"name": "Bob", "age": 25},
        ],
        [
            {"city": "Moscow", "year": 2024},
            {"city": "London", "year": 2025},
        ],
    ],
)
def test_json_to_csv_basic(tmp_path, data):
    src = tmp_path / "input.json"
    dst = tmp_path / "output.csv"

    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    json_to_csv(src, dst)

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == len(data)
    assert set(rows[0].keys()) == set(data[0].keys())

```



## Тест json_to_csv (файлы с неправильным содержанием)

```python
@pytest.mark.parametrize(
    "content",
    [
        "",
        "{}",
        "[]",
        "[1, 2, 3]",
    ],
)
def test_json_to_csv_invalid_json(tmp_path, content):
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"

    src.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(src, dst)
```


## Тест json_to_csv (с ошибками в пути файла/ неправильный тип файла)

```python
@pytest.mark.parametrize(
    "src_name, dst_name, error",
    [
        ("data.txt", "out.csv", ValueError),
        ("data.json", "out.txt", ValueError),
        ("missing.json", "out.csv", FileNotFoundError),
    ],
)
def test_json_to_csv_path_errors(tmp_path, src_name, dst_name, error):
    src = tmp_path / src_name
    dst = tmp_path / dst_name

    if src_name != "missing.json":
        src.write_text("[]", encoding="utf-8")

    with pytest.raises(error):
        json_to_csv(src, dst)
```

## Тест csv_to_json ( Обычные файлы)

```python
@pytest.mark.parametrize(
    "rows",
    [
        [
            {"name": "Alice", "age": "22"},
            {"name": "Bob", "age": "25"},
        ],
        [
            {"city": "Paris", "year": "2023"},
            {"city": "Berlin", "year": "2024"},
        ],
    ],
)
def test_csv_to_json_basic(tmp_path, rows):
    src = tmp_path / "input.csv"
    dst = tmp_path / "output.json"

    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(src, dst)

    data = json.loads(dst.read_text(encoding="utf-8"))

    assert data == rows
```



## Тест csv_to_json (файлы с неправильным содержанием)

```python
@pytest.mark.parametrize(
    "content",
    [
        "",
        "a,b,c",
    ],
)
def test_csv_to_json_invalid_csv(tmp_path, content):
    src = tmp_path / "bad.csv"
    dst = tmp_path / "out.json"

    src.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(src, dst)
```


## Тест csv_to_json (с ошибками в пути файла/ неправильный тип файла)

```python
@pytest.mark.parametrize(
    "src_name, dst_name, error",
    [
        ("data.txt", "out.json", ValueError),
        ("data.csv", "out.txt", ValueError),
        ("missing.csv", "out.json", FileNotFoundError),
    ],
)
def test_csv_to_json_path_errors(tmp_path, src_name, dst_name, error):
    src = tmp_path / src_name
    dst = tmp_path / dst_name

    if src_name != "missing.csv":
        src.write_text("a,b\n1,2", encoding="utf-8")

    with pytest.raises(error):
        csv_to_json(src, dst)
```

## Работа тестов:

<img width="1408" height="768" alt="тесты json_csv" src="https://github.com/user-attachments/assets/963f82e9-0a22-47df-97ce-b3e3d286b50a" />

##  Форматирование black:

<img width="683" height="122" alt="форматирование black" src="https://github.com/user-attachments/assets/bfd5529f-b216-448a-b5c7-dcde2dc368dd" />





<img width="1061" height="397" alt="image" src="https://github.com/user-attachments/assets/44079af8-bc33-4ad6-8f1a-a36000d169d2" />


# Лабораторная работа №8 по Python

## ООП в Python: @dataclass Student, методы и сериализация

## Задание A - class Students

```python
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверный формат даты рождения")

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должно быть от 0 до 5")

    def age(self) -> int:
        student_birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        now_date = datetime.today()
        age = now_date.year - student_birthdate.year
        if now_date.month < student_birthdate.month:
            age -= 1
        elif (
            now_date.month == student_birthdate.month
            and now_date.day < student_birthdate.day
        ):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        student = Student(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

        return student

    def __str__(self):
        return f"{self.fio}, {self.birthdate}, {self.group}, {self.gpa}"
```

```
Класс Student

A) Класс представляет информацию о студенте и включает поля:

1) fio — ФИО студента

2) birthdate — дата рождения в формате YYYY-MM-DD

3) group — учебная группа

4) gpa — средний балл (от 0 до 5)


B) При создании объекта выполняется проверка:

1) корректности формата даты рождения

2) допустимости значения GPA


C) Методы:

1) age() — вычисляет текущий возраст студента

2) to_dict() — возвращает данные студента в виде словаря

3) from_dict() — создаёт объект Student из словаря

4) __str__() — строковое представление студента
```

## Задание B - serialize.py

```python
import json
from .models import Student
from pathlib import Path


def students_to_json(students: list[Student], path: str | Path):
    data = [s.to_dict() for s in students]
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("В JSON должен лежать список студентов")
    students = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Информация о студенте должна храниться как словарь")
        student = Student.from_dict(item)
        students.append(student)
    return students

```

## students_input.json (входные данные):

<img width="809" height="943" alt="students_input json" src="https://github.com/user-attachments/assets/7e0e0522-46d1-4b51-9dc3-40e47464c205" />

## students_input.json (выходные данные после сериализации):

<img width="704" height="905" alt="students_output json" src="https://github.com/user-attachments/assets/260988ac-8588-4fbd-90c3-a13c6e906461" />


## тест  __post_init__:

``` 
У одного из студентов был введен gpa = 10, в students_input.json
```
<img width="1049" height="112" alt="проверка __post_init__" src="https://github.com/user-attachments/assets/28f0bc64-555d-45a2-8690-391017555115" />


## тест  age:

<img width="812" height="230" alt="проверка age" src="https://github.com/user-attachments/assets/1d4ea603-644a-4a11-a897-f9bf9eb5540f" />





# Лабораторная работа №10 по Python

## Структуры данных: Stack, Queue, Linked List и бенчмарки

## Краткая теоритическая справка
## Stack
```
Стек — линейная структура данных, работающая по принципу LIFO
(последний добавленный элемент извлекается первым).

Операции:
push — O(1)
pop — O(1)
peek — O(1)
```
## Queue
```
Очередь — линейная структура данных, работающая по принципу FIFO
(первый добавленный элемент извлекается первым).

Операции (на базе deque):
enqueue — O(1)
dequeue — O(1)
peek — O(1)

```
## Node
```
Node — элемент связного списка, содержащий значение и ссылку
на следующий узел.

Доступ к значению — O(1)
Переход к следующему узлу — O(1)

```
## Linked list
```
Односвязный список — структура данных, состоящая из узлов,
связанных ссылками.

Операции:
append — O(1)
prepend — O(1)
insert — O(n)
доступ по индексу — O(n)

```

## Задание A - Stack, Queue

## Код в structures.py

```
При попытке вернуть/удалить элемент из пустой структуры возращается None
```

```python
from collections import deque
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:

        if not self._data:
            return True
        return False

class Queue:
    def __init__(self):

        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            return None
        return self._data.popleft()

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data
```



## Задание B - Linked List

```
В Node добавлено поле tail (последний элемент)
```


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        self.tail = None

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self._size += 1
            if self.tail is None:
                self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):

        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

```

## Простые тесты работы структур

## Код в src/lab10/test.py

```python
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList, Node


print("Стек")
stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.is_empty():
    print("peek =", stack.peek(), "pop =", stack.pop())

print("Очередь")

queue = Queue()
for i in range(10):
    queue.enqueue(i)

while not queue.is_empty():
    print("peek =", queue.peek(), "dequeue =", queue.dequeue())

print("Односвязный список")

lst = SinglyLinkedList()

# append
for i in range(3):
    lst.append(i)
print("after append:", list(lst))

# prepend
lst.prepend(-1)
print("after prepend:", list(lst))

# insert
lst.insert(2, 99)
print("after insert:", list(lst))

# insert at edges
lst.insert(0, -2)
lst.insert(len(lst), 3)
print("after edge inserts:", list(lst))

# checks
print("size:", len(lst))
print("head:", lst.head.value)
print("tail:", lst.tail.value)


```
<img width="691" height="890" alt="test" src="https://github.com/user-attachments/assets/394e2931-a371-40ea-93be-0bb9b9d76cb7" />



## Benchmark

## Код в src/lab10/benchmark.py 

```python
import time
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList, Node
import random
N = 10000

# Stack
start = time.perf_counter()
s = Stack()
for i in range(N):
    s.push(i)
for i in range(N):
    s.pop()
print("Stack:", time.perf_counter() - start)

# Queue
start = time.perf_counter()
q = Queue()
for i in range(N):
    q.enqueue(i)
for i in range(N):
    q.dequeue()
print("Queue:", time.perf_counter() - start)

# Linked list append
start = time.perf_counter()
lst = SinglyLinkedList()
for i in range(N):
    lst.append(i)
print("LinkedList append:", time.perf_counter() - start)

# Linked list insert
start = time.perf_counter()
lst = SinglyLinkedList()
for i in range(N):
    lst.insert(i//2,i)
print("LinkedList insert:", time.perf_counter() - start)


```
<img width="461" height="199" alt="benchmark" src="https://github.com/user-attachments/assets/e9a8d274-bf6b-4e4f-b678-bc444ea7f422" />


```
Есть смысл сравнивать append в linked list и аналогичные операции в stack и queue.
Мы видим, что в stack и queue эти операции работают быстрее, тк:
1) узлы односвязного списка хранятся в памяти разрозненно, что увеличивает время
2) list и deque (на которых реализованы stack и queue) реализованы на C, что увеличивает оптимизацию

Операция insert в linked list работает сильно дольше из-за асимптоики O(n)
```





