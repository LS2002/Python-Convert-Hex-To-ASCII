#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#import regular expression
import re
import sys
import os

# print '6f'.decode('hex')

def main():
	#read file content
	if len(sys.argv)==2:
		raw_string = loadFile(sys.argv[1])
		replaceAllHexString(raw_string, findAllHexString(raw_string), 'converted.txt')
	else:
		print 'Usage error! \nUsage: python',os.path.basename(__file__),'<file-name-to-be-converted>'
		sys.exit(0)

def loadFile(fileName):
	raw_string = ''
	with open (fileName, "r") as myfile:
		raw_string = myfile.read().replace('\n', '')
	return raw_string

def findAllHexString(raw_string):
	completeHexCharacters  = []
	for character in re.findall('\\\\x[a-zA-Z0-9]{2}',raw_string):
		# print character[2:].decode('hex')
		completeHexCharacters.append(character[2:].decode('hex'))
	return list(set(completeHexCharacters))

def replaceAllHexString(raw_string, replaceList, newFileName):
	i=0
	while i<len(replaceList):
		raw_string = raw_string.replace('\\x'+replaceList[i].encode('hex'),replaceList[i])
		i += 1

	with open (newFileName, "w") as myfile:
		myfile.write(raw_string)


if __name__ == '__main__':
	main()
