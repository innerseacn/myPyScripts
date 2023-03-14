import pdfplumber
import csv


def pdf2csv(pdf_file, csv_file):
    # 使用pdfplumber打开pdf文件
    with pdfplumber.open(pdf_file) as pdf, open(csv_file, 'w') as c:
        writer = csv.writer(c)
        # 遍历pdf文件中的每一页
        for page in pdf.pages:
            # 提取每一页中的表格
            tables = page.extract_tables()
            # 遍历每一页中的每一个表格
            for table in tables:
                # 将表格保存为csv文件
                writer.writerows(table)


if __name__ == '__main__':
    pdf = "1.pdf"
    pdf2csv(pdf, f"{pdf}.csv")
    print('done')
