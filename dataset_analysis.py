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

def PNcount(labels):
	None	

if __name__ == '__main__':
	labels = read_labels('data/label.csv')
	sentences = read_raw('data/raw/*.sentence')
	consistency = check_consistency(sentences, labels)
	print(('not consist', 'consist')[consistency])
