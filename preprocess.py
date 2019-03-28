import csv, json
import os, sys
from glob import glob
from functools import cmp_to_key

def read_features(glob_condition = ''):
    print('read features' + '-' * 10)
    print('glob condition: %s' % glob_condition)
    features = []
    tokens = []
    target = glob(glob_condition)
    # target = sorted(target, key = lambda x:x.split('/')[-1].split('.')[-2])
    #target = sorted(target, cmp = lambda x, y: int(x.split('/')[-1].split('.')[-2]) - int(y.split('/')[-1].split('.')[-2]))
    target.sort(key = cmp_to_key(lambda x,y: int(x.split('/')[-1].split('.')[-2]) - int(y.split('/')[-1].split('.')[-2])))
    for i in target:
        print('open %s' % i)
        with open(i, 'r') as f:
            feat = json.loads(f.read())
            features.append(feat['vectors'])
            tokens.append(feat['tokens'])
    return features, tokens

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
    x = []
    y = []
    for i, j in zip(features, labels):
        print('feat len : %s' % str(len(i)))
        print('label len : %s' % str(len(j)))
        if(len(i) - 2 == len(j)):
            print('Append a right data')
            x.append(i)
            y.append(j)
    print('Now is having %s verified data' % str(len(x)))
    return x, y

if __name__ == '__main__':
    features, tokens = read_features(glob_condition = 'data/features/*.json')
    labels = read_labels(file_path = 'data/label.csv')
    features, labels = check_length(features, labels)
