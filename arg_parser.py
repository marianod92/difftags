# Python 3.8
# script.py
#!/usr/bin/env python
# coding: utf-8
import argparse

def execute_code(from_tag, to_tag):
    pass

def main():
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('from_tag', help='value of the first/least tag', type=str)
    parser.add_argument('to_tag', help='last/highest tag value', type=str)
    args = parser.parse_args()
    execute_code(args.from_tag, args.to_tag)

if __name__ == '__main__':
    main()