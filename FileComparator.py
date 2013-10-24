#FileComparator.py
import re,os

#import FolderDuplicates,SanitiseString

class FolderDuplicates():
	"""FolderDuplicates provides the logic to compare the contents any number of folder to find duplicates"""

	def __init__(self,folderPaths):
		self.folderPaths = {}
		self.folderContents = {}

		self.setFolderPaths(folderPaths)

	def printInfo(self):
		"prints infromation about the variable values of the class"

		print(self.folderPaths)
		print(self.folderContents)

	def setFolderPaths(self,folderPaths):
		"method to set the paths of the folder and then add the contents to the class"

		folderContents = self.folderContents
		currentFolderPaths = self.folderPaths

		for folderPath in folderPaths:
			folderName = directoryName(folderPath)
			folderContent = directoryContent(folderPath)
			folderContents[folderName] = folderContent
			currentFolderPaths[folderName] = folderPath

		self.folderPaths = currentFolderPaths
		self.folderContents = folderContents

	def sanitiseFolderContent(self,folderName,mode="film"):
		"sanitises the folder contents of the folder with the given name"

		sanitiseString = SanitiseString(mode)
		folderContents = self.folderContents

		sanitisedFolderContent = []
		for item in folderContents[folderName]:
			sanitisedFolderContent.append(sanitiseString.sanitise(item))

		folderContents[folderName] = sanitisedFolderContent
		self.folderContents = folderContents


	def getFolderContent(self,folderName):
		"returns the contents of the given folder"

		folderContents = self.folderContents
		return folderContents[folderName]


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
			self.replaceCharacters(["'"],"")
			self.replaceCharacters([".","  "]," ")
			self.removeBetween("[","]")
			self.removeBetween("(",")")

		return self.string

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

def directoryContent(path=None):
	"returns a list of all the files in the given path"

	if not path:
		path = os.getcwd()
	return os.listdir(path)

def directoryName(path=None):
	"returns the name of folder given by the path"

	if not path:
		path = os.getcwd()
	return os.path.split(path)[1]

def directorySize(path):
	"returns the size of the given path"

	if not path:
		path = os.getcwd()
	return os.path.getsize(path)

if __name__ == "__main__":
	folderA = r"E:\My Videos\My Films"
	folderB = r"E:\My Videos\NEW"
	folderDuplicates = FolderDuplicates([folderA,folderB])
	folderDuplicates.printInfo()
	folderDuplicates.sanitiseFolderContent("NEW")
	folderDuplicates.sanitiseFolderContent("My Videos")
	folderDuplicates.printInfo()

if __name__ != "__main__":
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