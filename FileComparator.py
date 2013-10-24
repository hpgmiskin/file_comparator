#FileComparator.py
import re

#import FolderDuplicates,SanitiseString

class FolderDuplicates():
	"""FolderDuplicates provides the logic to compare the contents any number of folder to find duplicates"""

	def __init__(self):
		print("SETUP")


class SanitiseString():
	"""SanitiseString provides the logic to remove unwanted content from string input"""

	def __init__(self,stringInput):
		self.string = stringInput

	def printString(self):
		print(self.string)


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
		

if __name__ == "__main__":

	sanitiseString = SanitiseString("""Test 'comma' [square] (bracket)""??,,*""")
	sanitiseString.printString()
	sanitiseString.replaceCharacters(["?",",","*","\""])
	sanitiseString.printString()
	sanitiseString.removeBetween("(",")")
	sanitiseString.printString()
	sanitiseString.removeBetween("[","]")
	sanitiseString.printString()
	sanitiseString.removeBetween("'","'")
	sanitiseString.printString()