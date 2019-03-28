import json

def read_train_data(file_path):
	print('Read train data ' + '-' * 10)
	features = []
	labels = []
	with open(file_path, 'r') as f:
		data = json.loads(f.read())
	for i in data:
		features.append(i['features'])
		labels.append(i['labels'])
	assert(len(features) == len(labels))
	return features, labels


if __name__ == '__main__':
	features, labels = read_train_data('data/train.json')
