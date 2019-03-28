import json

def read_train_data(file_path):
	with open(file_path, 'r') as f:
		data = json.loads(f.read())
	print(len(data))


if __name__ == '__main__':
	read_train_data('data/train.json')
