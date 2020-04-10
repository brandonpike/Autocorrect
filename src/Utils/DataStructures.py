#      [Author]
#    Brandon Pike
#      UTDallas
# Software Engineering

class Stack():
	def __init__(self):
		self.arr = []
	def put(self, obj):
		self.arr.append(obj)
	def pop(self):
		return self.arr.pop()
	def size(self):
		return len(self.arr)
	def printStack(self):
		print("[",end="")
		for a in arr:
			print(a + ",", end="")
		print("]")

class Trie:
	def __init__(self):
		self.tree = {}

	def backtrack(self, arr, cur, curPath, numFills):
		if numFills != -1 and len(arr) >= numFills:
			return
		temp = cur
		for n in cur:
			curPath = curPath + n
			cur = cur[n]
			if n == n.upper():
				arr.append(curPath)
			self.backtrack(arr, cur, curPath, numFills)
			cur = temp
			curPath = curPath[:-1]

	def autoFill(self, start, numFills=-1): # -1 means infinite
		arr = []
		cur = self.tree
		for lettr in start:
			if lettr not in cur:
				return arr
			cur = cur[lettr]
		b = self.backtrack(arr, cur, start, numFills)

		return arr

	def addWord(self, word):
		cur = self.tree
		for i,lettr in enumerate(word):
			if lettr.upper() not in cur and lettr.lower() not in cur:
				if i == len(word)-1:
					lettr = lettr.upper()
				cur[lettr] = {}
			elif i == len(word)-1:
				cur[lettr.upper()] = cur[lettr]
				cur.pop(lettr)
				return True
			cur = cur[lettr]

	def print(self):
		print(self.tree)