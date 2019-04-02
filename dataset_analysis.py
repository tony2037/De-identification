import os, sys
import csv
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
