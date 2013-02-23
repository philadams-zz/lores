lores
=====

Render images in the terminal. Pronounced 'Lo-Res'.

install
-------

`pip install lores`. Done.

TODO list requirements.

use
---

Render an image in your terminal:

    lores fixtures/sample.png

![example/example.png](./example/example.png)

help
----

As expected, via `-h` or `--help`:

    usage: lores [-h] imfile

    Render images on the terminal. http://github.com/philadams/lores

    positional arguments:
      imfile      image file to render

    optional arguments:
      -h, --help  show this help message and exit

future
------

- smarter image resizing
- intelligently handle remote requests or local files
