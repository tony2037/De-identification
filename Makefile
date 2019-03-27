PY = python3

# file: preprocess the files to raw data
file: file_preprocess.py
	$(PY) $<
preprocess: preprocess.py
	$(Make) -C bert all
	$(PY) $<

train: train.py
	$(PY) $<

evaluate: evaluate.py
	$(PY) $<
