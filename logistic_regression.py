import json
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score, f1_score, matthews_corrcoef
import numpy as np

def split():
	None

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

def average_list(l):
	average = 0.
	for i in l:
		average += i
	average = average / len(l)
	return average

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

	pred = np.array([]) # Prediction
	ground = np.array([]) # Ground true
	assert(Y_predict.shape[0] == Y_valid.shape[0])
	for i, j, k in zip(Y_valid, Y_predict, labels_padding[-(Y_valid.shape[0]):]):
		pred = np.append(pred, j[:-k])
		ground = np.append(ground, i[:-k])
	print(pred.shape)
	print(ground.shape)
	assert(pred.shape == ground.shape)
	return accuracy_score(ground, pred), roc_auc_score(ground, pred), recall_score(ground, pred), f1_score(ground, pred), matthews_corrcoef(ground, pred)
	'''
		accuracy.append(accuracy_score(i, j))
		try:
			roc_auc.append(roc_auc_score(i, j))
		except:
			print('Ground true is all 0, cannot calculate ROC_AUC')
			pass
		try:
			recall.append(recall_score(i, j))
		except:
			print('Devide 0')
			pass
		try:
			f1.append(f1_score(i, j))
		except:
			print('Devide 0')
			pass
		try:
			mc.append(matthews_corrcoef(i, j))
		except:
			print('Devide 0')
			pass
	average_acc = average_list(accuracy)
	average_roc = average_list(roc_auc)
	average_recall = average_list(recall)
	average_f1 = average_list(f1)
	average_mc = average_list(mc)
	print('The average accurracy is %s' % str(average_acc))
	print('The average ROC is %s' % str(average_roc))
	print('The average recall is %s' % str(average_recall))
	print('The average f1 is %s' % str(average_f1))
	print('The average mc is %s' % str(average_mc))
	return average_acc, average_roc, average_recall, average_f1, average_mc
	'''

if __name__ == '__main__':
	features, labels, features_padding, labels_padding = read_train_data('data/train.json')
	model, X_valid, Y_valid = logistic_model(features, labels)
	accurracy, roc, recall, f1, mc = model_evaluate(model, X_valid, Y_valid, labels_padding)
	print('accuracy: %s\nROC: %s\nRecall: %s\nF1: %s\nMCC: %s' % (str(accurracy), str(roc), str(recall), str(f1), str(mc)))
