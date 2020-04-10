from Utils.DataStructures import Trie

def getDictionary():
	arr = []
	file = open("../dictionary.txt", 'r')
	for i,line in enumerate(file):
		if "-" not in line:
			arr.append(line)
	return arr

def main():
	words = getDictionary()
	t = Trie()
	for word in words:
		t.addWord(word)

	inp = ""
	while(inp != "quit"):
		inp = input("Start typing to autofill..: ")
		options = t.autoFill(inp, 5)
		for option in options:
			print(option.lower())

if __name__ == '__main__':
	main()