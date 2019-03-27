PY = python3

file: file_preprocess.py
	$(PY) $<
preprocess: preprocess.py
	$(Make) -C bert all
	$(PY) $<

train: train.py
	$(PY) $<

evaluate: evaluate.py
	$(PY) $<
