from SanitiseString import SanitiseString
from SharedFunctions import *

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
		
		saveCSVFile("{} - {} - Duplicates.txt".format(folderNameA,folderNameB),duplicates)


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


if __name__ == "__main__":
	
	#define folders to compare
	folderA = r"test_folder/folder_a"
	folderB = r"test_folder/folder_b"

	#initiate class and set folder paths
	folderDuplicates = FolderDuplicates()
	folderDuplicates.setFolderPaths([folderA,folderB])

	#sanatise the file names in the folder using SanatiseString class
	folderDuplicates.sanitiseFolderContent("folder_a","film")
	folderDuplicates.sanitiseFolderContent("folder_b","film")

	#compare contents and output to csv file
	folderDuplicates.compareContents("folder_a","folder_b")

