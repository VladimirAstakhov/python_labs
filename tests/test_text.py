import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


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
