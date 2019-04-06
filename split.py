from script.read_data import read_data
from script.split_PN import split_PN
import sys, os
import json
import random

if __name__ == '__main__':
	sentences, labels = read_data()
	assert(len(sentences) == len(labels))
	positives, negatives = split_PN(sentences, labels)
	print('There are totally %s samples' % str(len(sentences)))
	print('There are:\n%s positive samples\n%s negative samples' %(str(len(positives)), str(len(negatives))))
	print('-' * 10)
	print('Randomly shuffle positive and negative samples')
	random.shuffle(positives)
	random.shuffle(negatives)
	print('-' * 10)
	ratio = 0.7
	print('Using ratio: %s to split data' % str(ratio))
	positive_train_number = int(len(positives) * ratio)
	positive_valid_number = len(positives) - positive_train_number
	negative_train_number = int(len(negatives) * ratio)
	negative_valid_number = len(negatives) - negative_train_number
	train_positives = positives[:positive_train_number]
	valid_positives = positives[positive_train_number:]
	train_negatives = negatives[:negative_train_number]
	valid_negatives = negatives[negative_train_number:]
	assert(len(valid_positives) == positive_valid_number)
	assert(len(valid_negatives) == negative_valid_number)
	print('-' * 10)
	print('Training data:')
	print('%s positive samples' % str(positive_train_number))
	print('%s negative samples' % str(negative_train_number))
	print('=' * 10)
	print('Validation data:')
	print('%s positive samples' % str(positive_valid_number))
	print('%s negative samples' % str(negative_valid_number))
	print('-' * 10)
	dataset_path = '/home/e24056310/De-identification/data/DEID'
	if (os.path.isdir(dataset_path)):
		print('directory exists')
	else:
		os.makedirs(dataset_path)
	print('All would be saved in %s' % dataset_path)
	print('-' * 10)
	with open(os.path.join(dataset_path, 'config.json'), 'w') as f:
		json.dump({'train':{'positives': positive_train_number, 'negatives': negative_train_number},\
			'valid':{'positives': positive_valid_number, 'negatives': negative_valid_number}}, f)
		f.close()
	with open(os.path.join(dataset_path, 'train.json'), 'w') as f:
		json.dump({'positives' : train_positives,\
			'negatives' : train_negatives},\
			 	f, ensure_ascii = False)
		f.close()
	with open(os.path.join(dataset_path, 'valid,json'), 'w') as f:
		json.dump({'positives' : valid_positives,\
			'negatives' : valid_negatives},\
			 	f, ensure_ascii = False)
		f.close()
	print('Three files has been generated in %s' % dataset_path)
	print('config.json')
	print('train.json')
	print('valid.json')
