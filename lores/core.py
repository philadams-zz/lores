#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Render images on the terminal.
"""

def main(args):

    # parse csv data
    rows = csv.reader(args.infile,
            delimiter=args.delimiter, quotechar=args.quotechar)

    # skip n rows
    for i in range(args.skip):
        rows.next()

    # prep fields
    if not args.fields:
        fields = ''
    fields = set([int(f) for f in args.fields.replace(' ', '').split(',')])

    # push to stdout
    out = csv.writer(sys.stdout)
    for row in pluck(rows, fields):
        out.writerow(row)


def cli():
    import argparse

    # populate and parse command line options
    desc = 'Render images on the terminal.'
    desc += '\nhttp://github.com/philadams/lores'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('imfile',
            help='image file to render')
    args = parser.parse_args()

    main(args)
