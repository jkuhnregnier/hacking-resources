#!/usr/bin/env python
# Relies on Python Version 2.7

from __future__ import print_function
import argparse
import sys
import string
import os.path
import random

def encipher(character):
	cipher = None
	try:
		cipher = cipherDict[character]
	except KeyError:
		substitutionChar = randomCharacter(character)
		cipherDict[character] = substitutionChar
		cipher = substitutionChar

	return cipher

def randomCharacter(character):
	if len(alphabetList) != 1:
		randomNum = random.randint(0, len(alphabetList)-1)
		randomChar = alphabetList[randomNum]

		# Avoid the case that the same character is returned as the given character itself
		while randomChar == character:
			randomNum = random.randint(0, len(alphabetList)-1)
			randomChar = alphabetList[randomNum]

	else:
		randomNum = 0
		randomChar = alphabetList[randomNum]

	alphabetList.remove(randomChar)		
	return randomChar

parser = argparse.ArgumentParser(description='Encipher a simple text.')
parser.add_argument('file', help='The file which contains the text to be encrypted')
parser.add_argument('-o', dest='outputFile', help='The output file which will contain the decoding table')
args = parser.parse_args()

alphabetList = list(string.ascii_lowercase)
cipherDict = {}
fh = ''
cipher = ''

if os.path.isfile(args.file):
	fh = open(args.file, 'r')
else:
	print("Could not read from text file. Please check whether it's a file.")
	sys.exit(0)

print("[*] Encrypting text...")
print("[*] Cipher text:")

while True:
	character = fh.read(1)

	if not character:
		break

	if character != " " and character != '.':
		cipher = encipher(character.lower())
	else:
		cipher = character
	print(cipher, end='') 
print('\n')

if args.outputFile: 
	fh = file.open(args.outputFile, 'w')
	for c in dictionary.keys:
		fh.write(c + ": " + dictionary[c])
	fh.close()
