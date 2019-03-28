import json
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
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
	model = LinearRegression()
	model.fit(X, Y)
	print(model.score(X, Y))
	return model

if __name__ == '__main__':
	features, labels = read_train_data('data/train.json')
	model = logistic_model(features, labels)
