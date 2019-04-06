def split_PN(sentences, labels):
	positives = []
	negatives = []
	for s, l in zip(sentences, labels):
		print(s)
		print(l)
		if(1 in l):
			print('Positive sample')
			positives.append((s, l))
		else:
			print('Negative sample')
			negatives.append((s, l))
	return positives, negatives
		
