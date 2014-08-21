import os,csv,json

def saveCsvFile(fileName,data):
	"saves the given list of lists as a CSV file"

	with open(fileName, 'w', newline='') as csvfile:
		csvWriter = csv.writer(csvfile, dialect="excel")

		for row in data:
			csvWriter.writerow(row)

def saveFile(fileName,data):
	"saves a file of a given name with the given variable"

	if (type(data) == str):
		saveData = data
	else:
		saveData = json.dumps(data)

	with open(fileName,"w") as openFile:
		openFile.write(saveData)

def loadFile(fileName,dataType="string"):
	"loads the file of the given name and returns the data"

	with open(fileName,"r") as openFile:
		loadData = openFile.read()

	if (dataType == "string"):
		data = loadData
	else:
		data = json.loads(loadData)

	return data

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