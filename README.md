# De-identification
de-identification NLP repo

## Explanation
* corpus: 王 小 明 想 要 借 錢
        (Wang Xiao Ming wants to borrow some money)
* label:  1  1  1 0  0  0  0
  * 王小明 is a name, which is considered as sort of private information, and can used to identify the person, 王小明.
  * 想要借錢: is not private information
* word embedding:
base on bert
        * [CLS] 王 小 明 想 要 借 錢 [SEP]
        * [768] x len(corpus + 2)
## Usage
### Install
`make install`
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
