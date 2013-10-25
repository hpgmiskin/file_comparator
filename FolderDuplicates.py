from SanitiseString import SanitiseString
from SharedFunctions import saveFile,loadFile,directoryContent,directoryName,directorySize

BACKUP_NAME = "FolderDuplicatesBackup.txt"

class FolderDuplicates():
	"""FolderDuplicates provides the logic to compare the contents any number of folder to find duplicates"""

	def __init__(self):
		self.folderPaths = {}
		self.folderContents = {}
		self.duplicates = {}

	def printInfo(self):
		"prints infromation about the variable values of the class"

		print(self.folderPaths)
		print(self.folderContents)

	def saveData(self):
		"method to save the class variables to a text document"

		folderPaths = self.folderPaths
		folderContents = self.folderContents
		duplicates = self.duplicates

		data = {"folderPaths":folderPaths,"folderContents":folderContents,"duplicates":duplicates}
		saveFile(BACKUP_NAME,data)

	def loadData(self):
		"method to load a backup of the class variabels into this instance of the class"

		data = loadFile(BACKUP_NAME,"json")

		self.folderPaths = data["folderPaths"]
		self.folderContents = data["folderContents"]
		self.duplicates = data["duplicates"]


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

	def findDuplicates(self,folderNameA,folderNameB):
		"method to find the films that are in both folders"

		folderContents = self.folderContents
		folderContentsA = folderContents[folderNameA]
		folderContentsB = folderContents[folderNameB]

		duplicates = [fileName for fileName in folderContentsA if fileName in folderContentsB]
		self.duplicates[folderNameA+" "+folderNameB] = duplicates

		return duplicates

	def getFolderContent(self,folderName):
		"returns the contents of the given folder"

		folderContents = self.folderContents
		return folderContents[folderName]


if __name__ == "__main__":
	folderDuplicates = FolderDuplicates()
	folderDuplicates.loadData()
	folderDuplicates.printInfo()

if __name__ != "__main__":
	folderA = r"E:\My Videos\My Films"
	folderB = r"E:\My Videos\NEW"
	folderDuplicates = FolderDuplicates()
	folderDuplicates.setFolderPaths([folderA,folderB])
	folderDuplicates.printInfo()
	folderDuplicates.sanitiseFolderContent("NEW")
	folderDuplicates.sanitiseFolderContent("My Films")
	folderDuplicates.printInfo()
	folderDuplicates.findDuplicates("NEW","My Films")
	folderDuplicates.saveData()
