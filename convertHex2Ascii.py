#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#import regular expression
import re
import sys

# print '6f'.decode('hex')

def main():
	#read file content
	if len(sys.argv)==2:
		raw_string = loadFile(sys.argv[1])
		findAllHexString(raw_string)
	else:
		sys.exit(0)

def loadFile(fileName):
	raw_string = ''
	with open (fileName, "r") as myfile:
		raw_string = myfile.read().replace('\n', '')
	return raw_string

def findAllHexString(raw_string):
	all = re.findall('x[a-zA-Z0-9]{2}',raw_string)
	print all

def findSubString(raw_string, start_marker, end_marker):
	return re.sub(
		r'\\x[a-zA-Z0-9]{2}'.format(re.escape(start_marker), re.escape(end_marker)),
		lambda m: m.group().strip().replace(' ', '_'),
		raw_string)

# brute force
def findSubString2(raw_string, start_marker, end_marker): 
	result = []
	rest = raw_string
	while True:
		head, sep, tail = rest.partition(start_marker)
		if not sep:
			break
		body, sep, tail = tail.partition(end_marker)
		if not sep:
			break
		result.append(head + start_marker + body.strip().replace(' ', '_') + end_marker)
		rest = tail
	result.append(rest)
	return ''.join(result)    

if __name__ == '__main__':
	main()
