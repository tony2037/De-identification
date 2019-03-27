import csv
from openpyxl import load_workbook

def read_labels(filename = 'data/label.csv'):
    print('read labels ---')
    labels = []
    with open(filename, newline = '') as f:
        raw = csv.reader(f)
        for i in raw:
            labels.append(i)
            print(i)
    return labels
def read_corpus(filename = 'data/sinopac_967.xlsx'):
    print('read corpuse')
    corpus = []
    wb = load_workbook(filename)
    sheets = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheets[0])
    for row in ws:
        for cell in row:
            corpus.append(cell.value)
            print(corpus[-1])

if __name__ == '__main__':
    read_labels('data/label.csv')
    read_corpus('data/sinopac_967.xlsx')
