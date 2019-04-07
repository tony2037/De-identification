import json
from script.read_data import read_dataset 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score, f1_score, matthews_corrcoef, precision_score
import numpy as np

def string_to_list(train, valid):
	for i in range(0, len(train)):
		train[i][0] = list(train[i][0])
		train[i][1] = np.asarray(train[i][1])
		assert(len(train[i][0]) == train[i][1].shape[0])
	for i in range(0, len(valid)):
		valid[i][0] = list(valid[i][0])
		valid[i][1] = np.asarray(valid[i][1])
		assert(len(valid[i][0]) == valid[i][1].shape[0])
	print(train)
	print(valid)
	return train, valid
		

if __name__ == '__main__':
	train, valid = read_dataset('/home/e24056310/De-identification/data/DEID1/train.json', '/home/e24056310/De-identification/data/DEID1/valid.json')
	train, valid = string_to_list(train, valid)
