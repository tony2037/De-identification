import threading
import sys, os
from bert_serving.client import BertClient

def server_activate():
	os.system('bert-serving-start -model_dir\
	/home/e24056310/De-identification/bert_embedding/chinese_L-12_H-768_A-12')

def client_activate():
	return BertClient()
