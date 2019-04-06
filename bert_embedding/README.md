# Activate server
`sh server_activate.sh`

# Word Embedding
```
from bert_embedding.bert_embedding import client_activate
BC = client_activate()
a = '測試'
a = list(a)
# ['測', '試']
vec = BC.encode(a)
print(type(vec))
# numpy.array
print(vec.shape)
# (2, 768)
```
