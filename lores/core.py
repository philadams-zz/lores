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

def main(args):

    #req = requests.get(args.imfile)
    #im = Image.open(StringIO(req.content))
    im = Image.open(args.imfile)
    maxw = 80
    im.thumbnail((40, 40), Image.ANTIALIAS)
    w, h = im.size
    pxs = im.load()
    for y in range(h):
        for x in range(w):
            px = pxs[x, y]
            sys.stdout.write(puts(px))
        sys.stdout.write('\n')

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
