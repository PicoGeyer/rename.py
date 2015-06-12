#!/bin/python2


try:
    import argparse
except:
    import pyargparse as argparse
import re
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--just-print', dest='just_print',
            action='store_true', default=False,
            help='Print out which files would be renamed instead of actually renaming any files')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
            default=False,
            help='Turn on verbose mode')
    parser.add_argument('regex', help='A python compatible regular expression')
    parser.add_argument('replace', 
        help='Replacement text for anything matching the regular expression')
    parser.add_argument('files', nargs='+', help='List of files to rename')
    args = parser.parse_args()
    for f in args.files:
        m = re.search(args.regex, f)
        if m:
            search_str = m.group()
            new_name =  f.replace(search_str, args.replace)
            if args.just_print:
                print(' {0} -> {1} '.format(f, new_name))
            else:
                os.rename(f, new_name)

if __name__ == '__main__':
    main()
