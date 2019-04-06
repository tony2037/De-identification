# De-identification
de-identification NLP repo

## Explanation
* corpus: 王 小 明 想 要 借 錢
        (Wang Xiao Ming wants to borrow some money)
* label:  1  1  1 0  0  0  0
  * 王小明 is a name, which is considered as sort of private information, and can used to identify the person, 王小明.
  * 想要借錢: is not private information
* word embedding (base on bert):
  * [CLS] 王 小 明 想 要 借 錢 [SEP]
  * [768] x (len(corpus) + 2)
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
### Logistic Regression
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

## Dataset analysis
### Use `dataset_analysis.py` to check details
`make statisitcs`
### The details
```
Positive samples: 2128
Negative samples: 160573
positive_sentences: 297
negative_sentences: 670
average proportion of overall: 0.02643522579731593
average proportion of only positive sentences: 0.08607024695624413
```
where:
* Positive samples means how many **characters** needed to be de-id there are in, while negative means not sensitive.
* Positive sentences stand for those sentences containing positive samples (positive characters), while negative stand for opposite side
* average proportion of overall: Take all porportions in consideration
* average proportion of only positive sentences: Take only positive sentences in account

## Dataset splitting
Split all of samples into train/valid with specific ratio(default : 0.7 / 0.3)
### `split.py`
```
make split
```
### Format
Under `data/` should be a `DEID/` directory,
in which contains three files:
#### `config.json`
```
{
"train":
        {"positives": number, "negatives": number}
"valid":
        {"positives": number, "negatives": number}
}
```
eg.
```
{"train": {"positives": 207, "negatives": 468}, "valid": {"positives": 90, "negatives": 202}}
```
#### `train.json`
```
{
'positives': [(sentences, labels), (), (), ...]
'negatives': [(snetences, labels), (), (), ...]
}
```
#### `valid.json`
```
{
'positives': [(sentences, labels), (), (), ...]
'negatives': [(snetences, labels), (), (), ...]
}
```
