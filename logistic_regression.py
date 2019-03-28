import json
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

def read_train_data(file_path):
	print('Read train data ' + '-' * 10)
	features = []
	labels = []
	with open(file_path, 'r') as f:
		data = json.loads(f.read())
	for i in data:
		features.append(i['features'])
		labels.append(i['labels'])
		for k in range(0, (128 - len(features[-1]))):
			features[-1].append([0.]* len(features[-1][0]))
		for k in range(0, (128 - len(labels[-1]))):
			labels[-1].append(0.)
	assert(len(features) == len(labels))
	return features, labels

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

def model_evaluate(model, X_valid, Y_valid):
	accuracy = []
	Y_predict = model.predict(X_valid)
	Y_predict = np.ceil(Y_predict)
	Y_predict = np.asarray(Y_predict, dtype=np.int32)
	Y_valid = np.asarray(Y_valid, dtype=np.int32)
	for i, j in zip(Y_valid, Y_predict):
		print(i)
		print(j)
		accuracy.append(accuracy_score(i, j))
		print(accuracy[-1])
	average_acc = 0.
	for i in accuracy:
		average_acc += i
	average_acc = average_acc / len(accuracy)
	print('The average accurracy is %s' % str(average_acc))
	return average_acc

if __name__ == '__main__':
	features, labels = read_train_data('data/train.json')
	model, X_valid, Y_valid = logistic_model(features, labels)
	accurracy = model_evaluate(model, X_valid, Y_valid)
