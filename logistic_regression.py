import json
from script.read_data import read_dataset 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score, f1_score, matthews_corrcoef, precision_score
import numpy as np



if __name__ == '__main__':
	train, valid = read_dataset('/home/e24056310/De-identification/data/DEID1/train.json', '/home/e24056310/De-identification/data/DEID1/valid.json')
