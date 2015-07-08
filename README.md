![Look, Ma! No deps!](https://raw.github.com/scardine/image_size/master/lookmanodeps.png)

Get image width and height given a file path using minimal dependencies (no need for PIL, libjpeg, libpng, etc).


Why don't you just use PIL?
---------------------------

PIL is huge and has lots of dependencies, may be an overkill if you just want the dimensions.
If you already have PIL installed, then sure, use it instead.

This was written in answer for the question "[Get Image size WITHOUT loading image into memory](http://stackoverflow.com/questions/15800704/python-get-image-size-without-loading-image-into-memory/)"
(using Python) in stackoverflow. The OP said:

> @PauloScardine hey thanks Paulo, this is great! It's always so nice to have code
that can be easily deployed without bringing in dependencies, and this fits the bill!
As you say, avoiding PIL is worth it for its own sake.

Usage
-----

Right now only for PNG, JPEG, GIF and BMP. Very untested, fork and send PRs.

    from get_image_size import get_image_size, UnknownImageFormat

    try:
        width, height = get_image_size('/path/to/image.ext')
    except UnknownImageFormat:
        width, height = -1, -1
