![Look, Ma! No deps!](https://raw.github.com/scardine/image_size/master/lookmanodeps.png)

Get image width and height given a file path using minimal dependencies (no need for PIL, libjpeg, libpng, etc).


Why don't you just use PIL?
---------------------------

PIL is huge and has lots of dependencies, perhaps an overkill if you want just the image dimensions.
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


Updates
-------

Over the time people sent updates for ".ico", ".bmp" and other improvements. It interesting to have all those algorithms in the same place so people can reimplement them using other languages, so thanks for all the pull requests (you can see the list of contributions in the history).

 > I added support for BMP file types, respecting different types of DIB headers. Should work on all current bitmap types, tested for old OS/2 and BITMAPCOREHEADER files, too. You might try it and consider it for merging if you find it useful. **No longer under 100 LOC though, sorry ;)**
 
Thanks
------

Thanks everyone who contributed with code or bug reports. You know who you are, THANK YOU!
