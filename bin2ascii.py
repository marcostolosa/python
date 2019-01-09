import binascii, sys

n = int(sys.argv[1], 2)
f = binascii.unhexlify('%x' % n)
print f