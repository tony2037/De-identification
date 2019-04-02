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
	positive_number = 0
	negative_number = 0
	for i in labels:
		for j in i:
			if(j == 1):
				positive_number += 1
			elif (j == 0):
				negative_number += 1
			else:
				print('label error')
				exit(-1)
	print('Positive samples: %s\nNegative samples: %s' %(str(positive_number), str(negative_number)))
	return positive_number, negative_number

def PNsentences(sentences, labels):
	positive_sentences = []
	negative_sentences = []
	proportions = []
	for s, l in zip(sentences, labels):
		if(1 in l):
			proportions.append(l.count(1) / len(l))
			positive_sentences.append((s, l))
		else:
			proportions.append(0)
			negative_sentences.append((s, l))
	print('positive_sentences: %s\nnegative_sentences: %s' %(str(len(positive_sentences)), str(len(negative_sentences))))
	return positive_sentences, negative_sentences, proportions

def proportion_detail(proportions):
	avg_overall = 0.
	avg_positive = 0.
	for p in proportions:
		avg_overall = avg_overall + p
		if (p is not 0):
			avg_positive = avg_positive + p
	avg_overall = avg_overall / len(proportions)
	avg_positive = avg_positive/ (len(proportions) - proportions.count(0))
	print('average proportion of overall: %s\naverage proportion of only positive sentences: %s' %(str(avg_overall), str(avg_positive)))
	return avg_overall, avg_positive

if __name__ == '__main__':
	labels = read_labels('data/label.csv')
	sentences = read_raw('data/raw/*.sentence')
	consistency = check_consistency(sentences, labels)
	print(('not consist', 'consist')[consistency])
	positive_number, negative_number = PNcount(labels)
	positive_sentences, negative_sentences, proportions = PNsentences(sentences, labels)
	proportion_overall, proportion_positive = proportion_detail(proportions)
