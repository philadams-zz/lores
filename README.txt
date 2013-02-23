lores
=====

Render images in the terminal. Pronounced 'Lo-Res'.

install
-------

`pip install lores`. Done.

TODO list requirements.

use
---

Render a local or remote image in your terminal:

    lores fixtures/parrot.png
    lores http://octodex.github.com/images/original.jpg

![example/example.png](./example/example.png)

help
----

As expected, via `-h` or `--help`:

    usage: lores [-h] [-w COLUMNS] imfile

    Render images on the terminal. http://github.com/philadams/lores

    positional arguments:
      imfile                image file to render

    optional arguments:
      -h, --help            show this help message and exit
      -c COLUMNS, --columns COLUMNS
                            width of img in terminal columns

future
------

- better error reporting (don't just defer to e.g. requests or PIL libs)
