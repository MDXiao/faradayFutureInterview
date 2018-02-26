#!/bin/python

from itertools import groupby
from collections import Counter 

class listManipulation :
	
	def __init__(self, argList):
		self.myList = argList

	def getList(self):
		return self.myList

	def storeItems(self, givenList):
		self.myList = givenList

	### I will consider unique items to be items that only appear once in the list
	def uniqueItems(self):
		return list(set(self.myList))

	def freqItems(self): # Just prints the most frequent items, no need to return anything
		retDict = {}
		# Counter sorts the list based on frequency for us. 
		for key, item in Counter(sorted(self.myList)).items(): 
			retDict[key] = item
		
		for key in sorted(retDict):
			print "%s: %s" % (key, retDict[key])

	def appendItem(self, toAppend):
		self.myList.append(toAppend)

	def insertItem(self, toInsert, position):
		self.myList.insert(toInsert, position)

if __name__ == "__main__":
	sampleList = [1,1,1,2,2,3,4,5,6,1,2,3,4,4543]
	test1 = listManipulation(sampleList)

	# Test cases for listManipulation class
	# print test1.getList()
	# test1.insertItem(0, 10000000000)
	# test1.insertItem(len(test1.getList()), 5000000000000)
	# test1.appendItem(1234123412341234)
	# print test1.getList()
	# test1.freqItems()

