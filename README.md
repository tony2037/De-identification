# De-identification
de-identification NLP repo

## Usage
### File preprocessing
`make file`
### Data preprocessing
including word embedding
`make preprocess`
### Logistic Regression
`make logistic`

## Data
in `data/`, `train.json` is a set of data going through preprocessing (including word embedding based on **Bert**)


## Records
### Regression
Using 70% of data as train data
The rest 30% as validation data
```
accuracy: 0.8349282296650717
ROC: 0.9156479217603912
Recall: 1.0
F1: 0.20689655172413793
MCC: 0.3097075252160898
Precision: 0.11538461538461539
```
