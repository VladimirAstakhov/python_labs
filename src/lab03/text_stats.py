from src.lib.text import normalize, count_freq, tokenize, top_n
import sys

# тесты normalize
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

# тесты tokenize
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

# тесты count_freq + top_n
tokens_1 = ["a", "b", "a", "c", "b", "a"]
freq_1 = count_freq(tokens_1)
print(freq_1, top_n(freq_1, 2))
tokens_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_2 = count_freq(tokens_2)
print(count_freq(tokens_2))
print(freq_2, top_n(freq_2, 2))

# Задание 2
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
