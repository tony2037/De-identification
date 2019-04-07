import csv, json
import os, sys
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
			labels.append([int(j) for j in i])
			print(labels[-1])
	return labels

def read_raw(glob_condition = ''):
	sentences = []
	targets = glob(glob_condition)
	targets.sort(key = lambda x: int(x.split('/')[-1].split('.')[-2]))
	for i in targets:
		print('Read: %s ...' % i)
		with open(i, 'r') as f:
			sentences.append(f.read())
			print(sentences[-1])
	return sentences

def check_consistency(sentences, labels):
	print('Check raw data and labels are matched to each other ?')
	for i, j in zip(sentences, labels):
		if(len(i) != len(j)):
			print('is not consist')
			print('Raw data(sentence) length: %s' % str(len(i)))
			print('Label length: %s' % str(len(j)))
			return False
	return True

def read_data(ask = False):
	ans = 'Y'
	sentences_glob = '/home/e24056310/De-identification/data/raw/*.sentence'
	labels_path = '/home/e24056310/De-identification/data/label.csv'
	if(ask):
		ans = ('N', 'Y')['Y' == input('sentences glob: %s? [Y]/N' % sentences_glob)]
		if (ans != 'Y'):
			sentences_glob = input('sentences glob?')
		ans = ('N', 'Y')['Y' == input('labels path: %s? [Y]/N' % labels_path)]
		if (ans != 'Y'):
			labels_path = input('labels path?')
	print('Using:\n%s as sentences glob condition\n%s as labels path' % (sentences_glob, labels_path))
	labels = read_labels(labels_path)
	sentences = read_raw(sentences_glob)
	if(check_consistency(sentences, labels)):
		print('Pass the test, all sentences length are matching labels')
		return sentences, labels
	else:
		print('Fail. inconsistent')
		return False

def read_dataset(train_json, valid_json):
	with open(train_json, 'r') as f:
		train = json.loads(f.read())
		f.close()
	with open(valid_json, 'r') as f:
		valid = json.loads(f.read())
		f.close()
	return train['positives'] + train['negatives'], valid['positives'] + valid['negatives']
