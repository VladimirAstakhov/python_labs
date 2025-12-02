import argparse
import sys
import os


from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Преобразует json файл в csv файл")
    p1.add_argument(
        "--in", dest="input", required=True, help="расположение входного файла"
    )
    p1.add_argument("--out", dest="output", required=True, help="место записи")

    p2 = sub.add_parser("csv2json", help="Преобразует csv файл в json файл")
    p2.add_argument(
        "--in", dest="input", required=True, help="расположение входного файла"
    )
    p2.add_argument("--out", dest="output", required=True, help="место записи")

    p3 = sub.add_parser("csv2xlsx", help="Преобразует csv файл в xlsx файл")
    p3.add_argument(
        "--in", dest="input", required=True, help="расположение входного файла"
    )
    p3.add_argument("--out", dest="output", required=True, help="место записи")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
