import argparse
from src.lib.text import normalize, count_freq, tokenize, top_n
import os

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()



    if args.command == "cat":
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")
        try:
            with open(args.input, "r", encoding="utf-8") as reader:
                reader = reader.read().splitlines()
        except:
            raise RuntimeError(f"Ошибка при чтении файла: {args.input}")
        for i in range(len(reader)):
            if (args.n):
                print(f"{i+1}: {reader[i]}")
            else:
                print(reader[i])
    elif args.command == "stats":
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")

        try:
            with open(args.input, "r", encoding="utf-8") as reader:
                reader = reader.read()
        except Exception:
            raise RuntimeError(f"Ошибка при чтении файла: {args.input}")
        text = normalize(reader)
        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, args.top)
        for word, number in top_words:
            print(f"{word}: {number}")
    else:
        raise parser.error("Не указана команда")


if __name__ == "__main__":
    main()
