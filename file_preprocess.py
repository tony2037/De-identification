import os, sys
import csv
from openpyxl import load_workbook
import glob

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
    print('read corpus ---')
    corpus = []
    wb = load_workbook(filename)
    sheets = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheets[0])
    for row in ws:
        for cell in row:
            corpus.append(cell.value)
            print(corpus[-1])
            print('-' * 10)
    return corpus
def corpus2txt(corpus):
    with open('data/corpus.txt', 'w') as f:
        for i in corpus:
            f.write(i)
            f.write('\n')
        f.close()
def corpus2raw(corpus, labels, start_number = 0):
    for i, j in zip(corpus, labels):
        assert(len(i) == len(j))
        with open('data/raw/%s.sentence' % str(start_number), 'w') as f:
            f.write(i)
            f.close
        start_number += 1
def feature_extract(input_file = '../data/corpus.txt'):
    os.chdir('./bert')
    command = 'python3 extract_features.py --input_file=../data/raw/0.sentence \
            --output_file=../data/features/0.json\
            --vocab_file=chinese_L-12_H-768_A-12/vocab.txt \
            --bert_config_file=chinese_L-12_H-768_A-12/bert_config.json \
            --init_checkpoint=chinese_L-12_H-768_A-12/bert_model.ckpt \
            --layers=-1,-2,-3,-4 \
            --max_seq_length=128 \
            --batch_size=8'
    print(command)
    os.system(command)


if __name__ == '__main__':
    """
    labels = read_labels('data/label.csv')
    corpus = read_corpus('data/sinopac_967.xlsx')
    corpus2txt(corpus)
    corpus2raw(corpus, labels, 0)
    """
    feature_extract()
