PY = python3

# file: preprocess the files to raw data
file: file_preprocess.py
	$(PY) $<
preprocess: preprocess.py
	$(PY) $<

# logistic: Doing logistic regression
logistic: logistic_regression.py
	$(PY) $<

# dataset analysis
statistics: dataset_analysis.py
	$(PY) $<

# split samples into train/valid dataset
split: split.py
	$(PY) $<

# pipline
train: train.py
	$(PY) $<

evaluate: evaluate.py
	$(PY) $<

# Install
install: requirement.txt
	pip3 install -r $<
