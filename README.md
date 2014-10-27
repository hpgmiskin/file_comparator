file_comparator
===============

This code is written to enable comparison of the contents of two folders and
there file contents. The primary design of these functions was to compare
folders with films contained within them.

To run the demo program which looks at folder_a and folder_b please type:

	python3 FolderDuplicates.py

This runs the code at the bottom of FolderDuplicates and will produce a csv
file that compares the folders contents. If this line fails to run then please
install python3 and for windows users add python to the PATH variable.

SharedFunctions
	Includes functions that are required by the other classes to operate
	correctly. This includes os calls to find the contents of folders along
	with functions to save and load data.

SanatiseString
	Includes a single class which is constructed with a string. The methods
	which are called allow the string to be reduced to its rawest form this
	means films can be compared without connecting words or symbols.

FolderDuplicates
	Includes a single class to compare the contents of folders.
	setFolderPaths is a method to configure the folder paths of interest.
	sanitiseFolderContent uses SanitiseString to sanitise all file names.
	compareContents produces a csv file to compare the contents of the folders