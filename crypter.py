#!/usr/bin/env python
import sys
import fileinput

def main():
    valid_operations = ['encrypt', 'decrypt']
    
    try:
        otp_filename = sys.argv[1]
        operation = sys.argv[2]
        if operation not in valid_operations:
            raise Exception
    except:
        print "Usage:"
        print "  {} <otp filename> <operation>".format(sys.argv[0])
        print "where operation in: {}, groups are newline seperated, and plain/cyphertext is fed to STDIN".format(str(valid_operations))
        sys.exit(1)

    try:
        with open(otp_filename, 'r') as otp:
            for input_group_raw in sys.stdin:
                input_group = input_group_raw.strip()
                otp_group = otp.readline().strip()
                if not otp_group:
                    otp.seek(0)
                    otp_group = otp.readline().strip()


                if operation == 'encrypt':
                    output = int(input_group) + int(otp_group)
                elif operation == 'decrypt':
                    output = int(input_group) - int(otp_group)
                else:
                    raise Exception('unrecognised operation')

                print str(output)
    except IOError as e:
        print 'Error reading file: {}'.format(otp_filename)
        sys.exit(1)


if __name__ == '__main__':
    main()
