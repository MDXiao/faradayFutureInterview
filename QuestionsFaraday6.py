#!/bin/python

import json # For JSON file handling
import sys # For GUI creation 
from PyQt4 import QtGui, QtCore ### Need to pip install gui library  

class CityInformation(QtGui.QWidget):
    
    def __init__(self, jsonData):
        super(CityInformation, self).__init__()
        # Initiate our GUI with the parsed JSON Dictionary and create the GUI on instiation
        self.jsonData = jsonData
        self.initUI(jsonData)

    def initUI(self, jsonData):

    	# Create Labels for drop box and text boxes
    	cityLabel = QtGui.QLabel('City')
    	countyLabel = QtGui.QLabel('County')
    	latLabel = QtGui.QLabel('Latitude')
    	longLabel = QtGui.QLabel('Longitude')

    	#Create boxes for the categories above
    	cityBox = QtGui.QComboBox(self)
    	self.countyBox= QtGui.QLineEdit()
    	self.latBox = QtGui.QLineEdit()
    	self.longBox = QtGui.QLineEdit()

    	#Create grid for alignment and spacing purposes
    	grid = QtGui.QGridLayout()
    	grid.setSpacing(20) #Sets spacing between widgets (horizontally)

    	#Add declared widgets - for city, county, latitude, and longitude
    	grid.addWidget(cityLabel, 1, 0)
    	grid.addWidget(cityBox, 1, 1)

    	grid.addWidget(countyLabel, 2, 0)
    	grid.addWidget(self.countyBox, 2, 1)

    	grid.addWidget(latLabel, 3, 0)
    	grid.addWidget(self.latBox, 3, 1)

    	grid.addWidget(longLabel, 4, 0)
    	grid.addWidget(self.longBox, 4, 1)

    	# Set the layout we declared above to the GUI
    	self.setLayout(grid)

    	# Populate the city drop box with our parsed JSON file entries
    	for key in self.jsonData.keys():
    		cityBox.addItem(key)

    	# To check if a city is selected from the drop box 
    	cityBox.activated[str].connect(self.onActivated)  

    	# Create window size (500 px by 300 px), and name our GUI
    	self.setGeometry(300,300,500,300)
    	self.setWindowTitle("City Information")
    	self.show()

    def onActivated(self, nameValue):
   		# Once a city is selected in the the combo box, set the value in the other fields
    	countyValue = self.jsonData[str(nameValue)][0]
    	self.latBox.setText(self.jsonData[str(nameValue)][1])
    	self.longBox.setText(self.jsonData[str(nameValue)][2])
    	
    	# Some of the cities had no county listed, so notifies the user if there is no county
    	# Also clears the county box, so no wrong listings are kept
    	if countyValue is not None:
    		self.countyBox.setText(countyValue)
    	else:
    		self.countyBox.setText("")
    		print "{name} does not have a county value".format(name=nameValue)
                
def main():
	
	data = json.load(open('ca.json')) ### Modularize this to take any user input
	#### data = json.load(open(argv[1]))
	#### Alternate method if we want the code to be able to accept any other similar JSON format!
	### Good for future usage

	jsonDict = {} ## Use  python dictionary, since access time is efficient and fast
	for val in range(0, len(data)):
		cityName = data[val]["name"]
		jsonDict[cityName] = []
		jsonDict[cityName].append(data[val]["county_name"])
		jsonDict[cityName].append(data[val]["primary_latitude"])
		jsonDict[cityName].append(data[val]["primary_longitude"])

	# Instiate a class to create an GUI object, and execute the application
	app = QtGui.QApplication(sys.argv)
	ex = CityInformation(jsonDict)
	sys.exit(app.exec_())

	# Close JSON file
	data.close()


if __name__ == '__main__':
    main()




