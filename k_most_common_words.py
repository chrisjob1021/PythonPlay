import string

words = { }

with open('text') as f:
	for line in f:
		l = line.split()
		for word in l:
			sw = word.lower().translate(None, string.punctuation)
			words[sw] = words.get(sw, 0) + 1

print sorted(words, key=words.get, reverse=True)[:10]
