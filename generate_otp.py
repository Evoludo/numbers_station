#!/usr/bin/env python
import random
import sys

def main():
    try:
        groups = int(sys.argv[1])
        if groups < 1:
            raise Exception
    except:
        print "Usage:"
        print "  {} <number of groups>".format(sys.argv[0])
        print "Where number of groups is the number of 5-digit to generate as a OTP"
        sys.exit(1)
    for group in range(groups):
        number = random.randrange(10000, 99900)
        print number

if __name__ == '__main__':
    main()
