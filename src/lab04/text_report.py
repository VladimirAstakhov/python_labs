
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

