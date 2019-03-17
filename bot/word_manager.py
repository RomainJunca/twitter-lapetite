def pick_word():
	words = None
	with open("./data/word_backlog.txt","r") as file:
		words = file.readlines()
	if len(words) < 1:
		raise Exception('No more word to pick')
	word = words.pop(0)
	with open("./data/word_backlog.txt","w") as file:
		for line in words:
			file.write(line)
	return word

def register_published(word, tweetid):
	with open("./data/word_published.txt","a") as file:
		file.write(str(tweetid)+" "+word)

