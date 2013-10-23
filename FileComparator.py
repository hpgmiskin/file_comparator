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

	def removeCharacters(self,characters):
		"method to strip class string of certain characters"

		oldString = self.string

		#pattern = re.escape(character)

		for character in characters:
			pattern = re.escape(character)
			newString = re.sub(pattern, "", oldString)
			oldString = newString
			#print(newString)

		self.string = newString


		

if __name__ == "__main__":

	sanitiseString = SanitiseString("""Test ()""??,,*""")
	sanitiseString.printString()
	sanitiseString.removeCharacters(["?",",","*","\"","(",")"])
	sanitiseString.printString()
