import re

class SanitiseString():
	"""SanitiseString provides the logic to remove unwanted content from string input"""

	def __init__(self,mode):
		self.mode = mode
		self.string = ""

	def printString(self):
		print(self.string)

	def sanitise(self,string):
		"method to return a sanitised string based on the class mode"

		self.string = string
		mode = self.mode

		if mode == "film":
			self.lowerCase()
			self.replaceCharacters(["'","?","!"],"")
			self.replaceCharacters([" and "," or "," of "," the "," & "]," ")
			self.replaceCharacters([".","-","   ","  "]," ")
			self.removeBetween("[","]")
			self.removeBetween("(",")")
			self.stripTrailing()

		return self.string

	def stripTrailing(self):
		"method to strip the trailling whitespace from the class string"

		oldString = self.string
		pattern = r'\s*$'
		newString = re.sub(pattern,"",oldString)
		self.string = newString
		return newString

	def lowerCase(self):
		"method to uncapitalise the given string"

		string = self.string
		self.string = string.lower()

	def removeBetween(self,openCharacter,closeCharacter):
		"method to remove the string between the given characters and the characters themselves"

		oldString = self.string
		pattern = re.compile("(\{}.*\{})".format(openCharacter,closeCharacter))
		matches = re.findall(pattern,oldString)
		self.replaceCharacters(matches)
		return matches

	def replaceCharacters(self,characters,substitute=""):
		"method to replace given characters in the class string with the given substitute"

		if (len(characters) < 1):
			return None

		oldString = self.string
		for character in characters:
			pattern = re.escape(character)
			newString = re.sub(pattern, substitute, oldString)
			oldString = newString

		self.string = newString
		return newString