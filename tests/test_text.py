import pytest
from src.lib.text import normalize


@pytest.mark.parametrize(
    "source_normalize, expected_normalize",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
@pytest.mark.parametrize(
    "source_tokenize, expected_tokenize",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source_normalize, expected_normalize):
    assert normalize(source_normalize) == expected_normalize
    pass


def test_tokenize_basic(source, expected):
    # TODO: Реализовать тесты токенизации
    pass


def test_count_freq_and_top_n():
    # TODO: Реализовать тесты частоты
    pass


def test_top_n_tie_breaker():
    # TODO: Реализовать тесты для топ_н
    pass
