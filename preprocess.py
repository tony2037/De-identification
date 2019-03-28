import csv, json
import os, sys
from glob import glob
from functools import cmp_to_key

import tensorflow as tf

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
            labels.append([float(j) for j in i])
            labels[-1]
    return labels

def check_length(features, labels, tokens):
    x = []
    y = []
    z = []
    for i, j, k in zip(features, labels, tokens):
        print('feat len : %s' % str(len(i)))
        print('label len : %s' % str(len(j)))
        if(len(i) - 2 == len(j)):
            print('Append a right data')
            x.append(i)
            y.append(j)
            z.append(k)
    print('Now is having %s verified data' % str(len(x)))
    return x, y, z

def data2TFRecord(features, labels, file_path):
    writer = tf.python_io.TFRecordWriter(file_path)
    features_tf = []
    for i in features:
        features_tf.append(tf.train.FloatList(value=[i]))
    for x, y in zip(features_tf, labels):
        print(x)
        print(y)
        example = tf.train.Example(features=tf.train.Features(feature={\
                'label': tf.train.Feature(float_list=tf.train.FloatList(value=y)),\
                'feature': tf.train.Feature(float_list=tf.train.FloatList(value=[x]))\
            }))
        writer.write(example.SerializeToString())
    writer.close()

def data2json(features, labels, tokens, file_path):
    data = []
    for i, j, k in zip(features, labels, tokens):
        data.append({'features': i, 'labels': j, 'tokens': k})
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii = False)

if __name__ == '__main__':
	features, tokens = read_features(glob_condition = 'data/features/*.json')
	labels = read_labels(file_path = 'data/label.csv')
	features, labels, tokens = check_length(features, labels, tokens)
	data2json(features, labels, tokens, 'data/train.json')
        # data2TFRecord(features, labels, 'data/train.tfrecords')
