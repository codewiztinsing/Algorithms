#find all occurence of given word from sentance

stat = "this is me this is you"
word = "is"

def find_all(word,stat):
	i = 0
	count = 0
	while i < len(stat):
		begin_index = 0
		move = len(word)
		word_to_compare = stat[begin_index,move]
		if word == word_to_compare:
			count = count + 1


		i = i + 1

	


find_all(word,stat)
