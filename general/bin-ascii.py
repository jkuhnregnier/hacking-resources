#!/bin/usr/env python

import binascii

filename = 'lorem.txt'
fh = open(filename, 'rb')

try: 
	byte = fh.read(1)
	while byte != "":
		n = bin(int(binascii.hexlify(byte), 16))
		print "Read '"+byte+"' as " + n

		byte = fh.read(1)
finally:
	fh.close()

def binaryToChar(binary):
	bin_int = int(binary, 2)
	return binascii.unhexlify('%x' % bin_int)


# Resources to read more on this topic
# ------------------------------------

# https://docs.python.org/2/library/binascii.html
# https://stackoverflow.com/questions/35063732/binary-to-ascii-in-python
# https://stackoverflow.com/questions/37590412/converting-binary-to-ascii-and-ascii-to-binary
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa