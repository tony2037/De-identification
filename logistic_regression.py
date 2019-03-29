import json
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score, f1_score, matthews_corrcoef, precision_score
import numpy as np

def split():
	None
'''
Read train data from json file
the format should be
[ele, ele, ele ...]
ele = {'features': (l + 2, 768), 'labels': (l,)}
l: The length of corpus, +2 because of [CLS] [SEP] coming after going through bert
@file_path: The path of json file
'''
def read_train_data(file_path):
	print('Read train data ' + '-' * 10)
	features = []
	labels = []
	features_padding = []
	labels_padding = []
	with open(file_path, 'r') as f:
		data = json.loads(f.read())
	for i in data:
		if(len(i['features']) > 128 or len(i['labels']) > 128):
			print('the length is bigger than 128')
			split()
			continue
		features.append(i['features'])
		labels.append(i['labels'])
		features_padding.append(128 - len(features[-1]))
		labels_padding.append(128 - len(labels[-1]))
		for k in range(0, (128 - len(features[-1]))):
			features[-1].append([0.]* len(features[-1][0]))
		for k in range(0, (128 - len(labels[-1]))):
			labels[-1].append(0.)
	assert(len(features) == len(labels))
	return features, labels, features_padding, labels_padding

'''
Using linear regression to fit
@features: The input of the model, which are word embedding right here
@labels: The output of the model, which are ground truth
'''
def logistic_model(features, labels):
	print('Train ' + '.' * 10)
	X = []
	Y = []
	for i, j in zip(features, labels):
		X.append(np.array(i, dtype=np.float32))
		Y.append(np.array(j, dtype=np.float32))
	X = np.asarray(X, dtype=np.float32)
	Y = np.asarray(Y, dtype=np.float32)
	print('The X and Y shape before reshape ...')
	print(X.shape)
	print(Y.shape)
	X = X.reshape((X.shape[0], X.shape[1] * X.shape[2])) # Because sklearn only accept 2d input data
	print('The shape after reshape')
	print(X.shape)
	print('The total data is %s' % str(X.shape[0]))
	train_num = int(X.shape[0] * 0.7)
	valid_num = X.shape[0] - train_num
	X_train = X[:train_num]
	X_valid = X[train_num:]
	Y_train = Y[:train_num]
	Y_valid = Y[train_num:]
	print('The number of train set is %s' % str(train_num))
	print('The number of valid set is %s' % str(valid_num))
	assert(X_train.shape[0] == Y_train.shape[0])
	assert(X_valid.shape[0] == Y_valid.shape[0])
	print('The X_train shape is %s' % str(X_train.shape))
	print('The Y_train shape is %s' % str(Y_train.shape))
	model = LinearRegression()
	model.fit(X, Y)
	print(model.score(X, Y))
	return model, X_valid, Y_valid

'''
Calculate average of a list
'''
def average_list(l):
	average = 0.
	for i in l:
		average += i
	average = average / len(l)
	return average

'''
Evaluate model with several common indicators
@model: The model to be evaluated
@X_valid: Features
@Y_valid: Labels
@labels_padding: The record of padding, which is used for removing padding
'''
def model_evaluate(model, X_valid, Y_valid, labels_padding):
	np.seterr(all='raise') # Treat all warnings as exception
	warnings.filterwarnings('error')
	accuracy = [] # accuracy
	roc_auc = [] # Area under ROC curve
	recall = [] # Rceall
	f1 = [] # F1 score
	mc = [] # Matthews_corrcoef
	Y_predict = model.predict(X_valid)
	Y_predict = Y_predict / np.linalg.norm(Y_predict)
	Y_predict = np.ceil(Y_predict)
	Y_predict = np.asarray(Y_predict, dtype=np.int32)
	Y_valid = np.asarray(Y_valid, dtype=np.int32)

	pred = np.array([], dtype=np.int32) # Prediction
	ground = np.array([], dtype=np.int32) # Ground true
	assert(Y_predict.shape[0] == Y_valid.shape[0])
	for i, j, k in zip(Y_valid, Y_predict, labels_padding[-(Y_valid.shape[0]):]):
		pred = np.append(pred, j[:-k])
		ground = np.append(ground, i[:-k])
	print(pred.shape)
	print(ground.shape)
	print(pred)
	print(ground)
	assert(pred.shape == ground.shape)
	return accuracy_score(ground, pred), roc_auc_score(ground, pred), recall_score(ground, pred),\
		f1_score(ground, pred), matthews_corrcoef(ground, pred), precision_score(ground, pred)

if __name__ == '__main__':
	features, labels, features_padding, labels_padding = read_train_data('data/train.json')
	model, X_valid, Y_valid = logistic_model(features, labels)
	accurracy, roc, recall, f1, mc, precision = model_evaluate(model, X_valid, Y_valid, labels_padding)
	print('accuracy: %s\nROC: %s\nRecall: %s\nF1: %s\nMCC: %s\nPrecision: %s' % (str(accurracy), str(roc), str(recall), str(f1), str(mc), str(precision)))
