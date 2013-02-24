lores
=====

Render images in the terminal. Pronounced 'Lo-Res'.

install
-------

`pip install lores`. Done.

lores depends on [pillow][], [requests][], and [vari][]; the above
command installs dependencies as needed.

[pillow]: https://github.com/python-imaging/Pillow
[requests]: https://github.com/kennethreitz/requests
[vari]: https://github.com/philadams/vari

use
---

Render a local or remote image in your terminal:

    lores fixtures/parrot.png
    lores --columns=40 http://octodex.github.com/images/original.jpg

![example/example.png](./example/example.png)

help
----

As expected, via `-h` or `--help`:

    usage: lores [-h] [-c COLUMNS] imfile

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
