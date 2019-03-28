import csv
import os, sys
from glob import glob

def read_features(glob_condition = ''):
    print('read features' + '-' * 10)
    print('glob condition: %s' % glob_condition)
    features = []
    for i in glob(glob_condition):
        with open(i, 'r') as f:
            feat = json.loads(f.read())
            features.append(feat['vectors'])
    return features

def read_labels(file_path = ''):
    print('read labels' + '-' * 10)
    labels = []
    with open(file_path, newline = '') as f:
        raw = csv.reader(f)
        for i in raw:
            labels.append(i)
            print(i)
    return labels

def check_length(features, labels):
    for i, j in zip(features, labels):
        assert(len(i) == len(j))

if __name__ == '__main__':
    features = read_features(glob_condition = 'data/features/*.sentence')
    labels = read_labels(file_path = 'data/label.csv')
    check_length(features, labels)
