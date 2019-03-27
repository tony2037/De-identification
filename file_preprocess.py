import os, sys
import csv
from openpyxl import load_workbook
from glob import glob

'''
Read the labels from the file
@filename: the .csv file containing labels
'''
def read_labels(filename = 'data/label.csv'):
    print('read labels ---')
    labels = []
    with open(filename, newline = '') as f:
        raw = csv.reader(f)
        for i in raw:
            labels.append(i)
            print(i)
    return labels

'''
Read the corpus from the file
@filename: the .xlsx file containing corpus
'''
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

'''
Convert corpus to .txt file
@corpus: corpus read from the file
'''
def corpus2txt(corpus):
    with open('data/corpus.txt', 'w') as f:
        for i in corpus:
            f.write(i)
            f.write('\n')
        f.close()

'''
Convert corpus to raw data
@corpus: corpus
@labels: labels
@start_number: the index number of raw data, e.g 0 means the first output raw data is 0, and 1 is following
'''
def corpus2raw(corpus, labels, start_number = 0):
    for i, j in zip(corpus, labels):
        assert(len(i) == len(j))
        with open('data/raw/%s.sentence' % str(start_number), 'w') as f:
            f.write(i)
            f.close
        start_number += 1

'''
Word embedding: Based on Bert
@glob_condition: glob condition, eg.path/to/file/*.sentence
'''
def feature_extract(glob_condition = ''):
    sentences = []
    for i in glob(glob_condition):
        sentences.append(i.split('/')[-1])
        print(sentences[-1])

    os.chdir('./bert')
    for i in sentences:
        print(i.split('.')[0])
        command = 'python3 extract_features.py --input_file=../data/raw/%s \
            --output_file=../data/features/%s.json\
            --vocab_file=chinese_L-12_H-768_A-12/vocab.txt \
            --bert_config_file=chinese_L-12_H-768_A-12/bert_config.json \
            --init_checkpoint=chinese_L-12_H-768_A-12/bert_model.ckpt \
            --layers=-1,-2,-3,-4 \
            --max_seq_length=128 \
            --batch_size=8' % (i, i.split('.')[0])
        print(command)
        os.system(command)


if __name__ == '__main__':
    """
    labels = read_labels('data/label.csv')
    corpus = read_corpus('data/sinopac_967.xlsx')
    corpus2txt(corpus)
    corpus2raw(corpus, labels, 0)
    """
    feature_extract(glob_condition = 'data/raw/*.sentence')
