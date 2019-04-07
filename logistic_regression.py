from script.read_data import read_dataset 
from bert_embedding.bert_embedding import client_activate, server_terminate

import numpy as np
import json

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score, f1_score, matthews_corrcoef, precision_score

BC = None

def string_to_list(train, valid):
	for i in range(0, len(train)):
		# Because Bert dose not accept empty character
		train[i][0] = train[i][0].replace(' ', ',')
		train[i][0] = list(train[i][0])
		train[i][1] = np.asarray(train[i][1])
		assert(len(train[i][0]) == train[i][1].shape[0])
	for i in range(0, len(valid)):
		# Because Bert dose not accept empty character
		valid[i][0] = valid[i][0].replace(' ', ',')
		valid[i][0] = list(valid[i][0])
		valid[i][1] = np.asarray(valid[i][1])
		assert(len(valid[i][0]) == valid[i][1].shape[0])
	print(train)
	print(valid)
	return train, valid

def word2vec_bert(train, valid):
	global BC
	for i in range(0, len(train)):
		train[i][0] = BC.encode(train[i][0])
		assert(train[i][0].shape[0] == train[i][1].shape[0])
	for i in range(0, len(valid)):
		valid[i][0] = BC.encode(valid[i][0])
		assert(valid[i][0].shape[0] == valid[i][1].shape[0])
	print(train)
	print(valid)
	return train, valid

if __name__ == '__main__':
	train, valid = read_dataset('/home/e24056310/De-identification/data/DEID1/train.json', '/home/e24056310/De-identification/data/DEID1/valid.json')
	train, valid = string_to_list(train, valid)
	BC = client_activate()
	train, valid = word2vec_bert(train, valid)
