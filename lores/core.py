#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Render images on the terminal.
"""

import sys
from StringIO import StringIO

from PIL import Image
import requests
import vari


def puts(clr):
    c = vari.Vari(rgb=clr)
    fmt = '\x1b[48;5;%sm  \x1b[0m'
    return fmt % c.x256


def flush(im):
    w, h = im.size
    pxs = im.load()
    alpha = len(pxs[0, 0]) == 4
    for y in range(h):
        for x in range(w):
            px = pxs[x, y]
            if alpha and px[3] < 128:
                sys.stdout.write('  ')
            else:
                sys.stdout.write(puts(px[:3]))
        sys.stdout.write('\n')


def main(args):

    if args.imfile.startswith('http'):
        req = requests.get(args.imfile)
        im = Image.open(StringIO(req.content))
    else:
        im = Image.open(args.imfile)

    maxw = int(args.columns / 2)
    maxh = int(maxw * (float(im.size[1]) / im.size[0]))
    maxsize = maxw if maxw > maxh else maxh
    im.thumbnail((maxsize, maxsize), Image.ANTIALIAS)
    flush(im)


def cli():
    import argparse

    # populate and parse command line options
    desc = 'Render images on the terminal.'
    desc += '\nhttp://github.com/philadams/lores'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('imfile',
                        help='image file to render')
    parser.add_argument('-c', '--columns', dest='columns', type=int,
                        default=80, help='width of img in terminal columns')
    args = parser.parse_args()

    main(args)
