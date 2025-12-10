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


