PY = python3

preprocess: preprocess.py
	$(PY) $<

train: train.py
	$(PY) $<

evaluate: evaluate.py
	$(PY) $<
