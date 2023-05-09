#!/usr/bin/python3
for alphas in range(97, 123):
    if chr(alphas) is not 'q' and chr(alphas) is not 'e':
	print("{:c}".format(alphas), end='')
