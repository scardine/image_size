

================
get_image_size
================
| Src: https://github.com/scardine/image_size
| PyPI:

.. image:: https://raw.github.com/scardine/image_size/master/lookmanodeps.png
    :alt: Look, Ma! No deps!

Get image width and height given a file path using minimal dependencies
(no need for PIL, libjpeg, libpng, etc).


Why don't you just use PIL?
---------------------------

PIL is huge and has lots of dependencies, perhaps an overkill if you
want just the image dimensions.  If you already have PIL installed, then
sure, use it instead.

This was written in answer for the question "`Get Image size WITHOUT
loading image into memory
<http://stackoverflow.com/questions/15800704/python-get-image-size-without-loading-image-into-memory/>`__"
(using Python) in stackoverflow. The OP said:

    @PauloScardine hey thanks Paulo, this is great!  It's always so nice
    to have code that can be easily deployed without bringing in
    dependencies, and this fits the bill!  As you say, avoiding PIL is
    worth it for its own sake.

Usage
-----

Right now only for PNG, JPEG, GIF, BMP and TIF. Very untested, fork and
send PRs.

Python ``get_image_size.get_image_size`` usage:

.. code:: python

    import get_image_size
    try:
        width, height = get_image_size.get_image_size('/path/to/image.ext')
    except get_image_size.UnknownImageFormat:
        width, height = -1, -1


Python ``get_image_size.get_image_metadata`` usage:

.. code:: python

   import get_image_size
   try:
       img = get_image_size.get_image_metadata('/path/to/image.ext')
       width, height = img.width, img.height
       print(img._asdict())
   except get_image_size.UnknownImageFormat:
       width, height = -1, -1

Commandline ``get-image-size`` usage:

.. code:: bash

    $ python -m get_image_size --help
    $ get-image-size --help
    Usage: get-image-size [-v|--verbose] [--json|--json-indent] <path0> [<pathN>]

    Print metadata for the given image paths (without image library bindings).

    Options:
      -h, --help     show this help message and exit
      --json
      --json-indent
      -v, --verbose
      -q, --quiet
      -t, --test

    $ get-image-size ./lookmanodeps.png
    251	208	22228	PNG	./lookmanodeps.png

    $ get-image-size --json-indent ./lookmanodeps.png
    {
      "path": "./lookmanodeps.png",
      "type": "PNG",
      "file_size": 22228,
      "width": 251,
      "height": 208
    }




Updates
-------

Over the time people sent updates for ".ico", ".bmp" and other
improvements. It is interesting to have all those algorithms in the same
place so people can reimplement them using other languages, so thanks
for all the pull requests (you can see the list of contributions in the
history).

    I added support for BMP file types, respecting different types of
    DIB headers. Should work on all current bitmap types, tested for old
    OS/2 and BITMAPCOREHEADER files, too. You might try it and consider
    it for merging if you find it useful. **No longer under 100 LOC
    though, sorry ;)**


License
--------

MIT License


Thanks
------

Thanks everyone who inspired this, contributed with code or sent bug
reports. You know who you are, THANK YOU!
