import argparse
import pdfplumber
import csv
from tqdm import tqdm


def pdf2csv(pdf_file, csv_file):
    with pdfplumber.open(pdf_file) as pdf, open(csv_file, 'w') as c:
        writer = csv.writer(c)
        for page in tqdm(pdf.pages):
            for table in page.extract_tables():
                writer.writerows(table)
            page.flush_cache() # 清空缓存，否则页面过多会直接拉爆内存。


if __name__ == '__main__':
    # pdf = 'z:/1.pdf'
    parser = argparse.ArgumentParser(
                    prog='pdf2csv.py',
                    description='Extract tables in pdf file and save as csv file',
                    epilog='InnerSea at 2023-3-14')
    parser.add_argument('pdf', help='pdf file path')
    pdf = parser.parse_args().pdf
    pdf2csv(pdf, f"{pdf}.csv")
