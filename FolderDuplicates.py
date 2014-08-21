from SanitiseString import SanitiseString
from SharedFunctions import *#saveFile,loadFile,directoryContent,directoryName,directorySize

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
		print(duplicates)
		saveFile("{} - {} - Duplicates.txt".format(folderNameA,folderNameB),duplicates)

		return duplicates

	def compareContents(self,folderNameA,folderNameB):
		"method to compare the contents of two folders and write a csv file with the comparison"

		folderContents = self.folderContents
		folderContentsA = folderContents[folderNameA]
		folderContentsB = folderContents[folderNameB]

		folderContentsA = sorted(folderContentsA)
		folderContentsB = sorted(folderContentsB)

		output = []
		output.append([folderNameA,folderNameB])

		#while the folders still have contents to compare
		while (sum([len(folderContentsA),len(folderContentsB)]) > 0):

			#if there is nothing in folder A write folder B
			if (len(folderContentsA) == 0):
				output.append(["",folderContentsB.pop(0)])
			#if there is nothin in folder B write folder A
			elif (len(folderContentsA) == 0):
				output.append([folderContentsA.pop(0),""])
			#if the folder contents is the same write both
			elif (folderContentsA[0] == folderContentsB[0]):
				output.append([folderContentsA.pop(0),folderContentsB.pop(0)])
			#otherwise take the folder contents wich is higher in the alphabet
			elif (sorted([folderContentsA[0],folderContentsB[0]])[0] == folderContentsA[0]):
				output.append([folderContentsA.pop(0),""])
			else:
				output.append(["",folderContentsB.pop(0)])

		#save the file to csv
		saveCsvFile("{} - {} - Comparison.csv".format(folderNameA,folderNameB),output)


	def getFolderContent(self,folderName):
		"returns the contents of the given folder"

		folderContents = self.folderContents
		return folderContents[folderName]


if False:
	folderDuplicates = FolderDuplicates()
	folderDuplicates.loadData()
	folderDuplicates.printInfo()
else:
	folderA = r"E:\My Videos\My External Films"
	folderB = r"D:\Videos\My Films"

	folderDuplicates = FolderDuplicates()
	folderDuplicates.setFolderPaths([folderA,folderB])

	folderDuplicates.sanitiseFolderContent("My External Films")
	folderDuplicates.sanitiseFolderContent("My Films")
	folderDuplicates.compareContents("My External Films","My Films")

