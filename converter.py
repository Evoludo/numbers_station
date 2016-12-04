#!/usr/bin/env python
import sys


def main():
    valid_operations = ['encode', 'decode']

    try:
        operation = sys.argv[1]
        if operation not in valid_operations:
            raise Exception
    except:
        print "Usage:"
        print "  {}  <operation>".format(sys.argv[0])
        print "where operation in: {}, and data is fed to STDIN".format(str(valid_operations))
        sys.exit(1)

    base = ord('A') - 1
    if operation == 'encode':
        for line_raw in sys.stdin:
            line = line_raw.strip().upper()
            for char in line:
                if char.isalpha():
                    output = ord(char) - base
                elif char == ' ':
                    output = 27
                else:
                    continue
                print output
    elif operation == 'decode':
        output = ''
        for line_raw in sys.stdin:
            offset = int(line_raw.strip())
            if offset == 27:
                char = ' '
            else:
                char = chr(base + offset)
            output += char
        print output
    else:
        raise Exception('Unrecognised operation')

if __name__ == '__main__':
    main()
