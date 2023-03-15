# *--codeing: utf-8--*

import argparse
import csv
import pdfplumber
from tqdm import tqdm


def pdf_to_table_list(pdf_file) -> list[list]:
    with pdfplumber.open(pdf_file) as pdf:
        tables = []
        for page in tqdm(pdf.pages, desc="Extracting tables in PDF: "):
            tables.extend(page.extract_tables())
            page.flush_cache()  # 清空缓存，否则页面过多会直接拉爆内存。
        return tables


def table_list_to_csv(csv_file, tables: list[list]) -> None:
    with open(csv_file, 'w') as c:
        writer = csv.writer(c)
        for table in tqdm(tables, desc="Writing into CSV: "):
            writer.writerows(table)


if __name__ == '__main__':
    # pdf = 'z:/1.pdf'
    parser = argparse.ArgumentParser(
        prog='pdf2csv.py',
        description='Extract tables in pdf file and save as csv file',
        epilog='InnerSea at 2023-3-14')
    parser.add_argument('pdf', help='pdf file path')
    pdf = parser.parse_args().pdf
    table_list_to_csv(f"{pdf}.csv", pdf_to_table_list(pdf))
