![Look, Ma! No deps!](https://raw.github.com/scardine/image_size/master/lookmanodeps.png)


image_size
==========

Get image width and height given a file path using minimal dependencies (no need for PIL, libjpeg, libpng, etc).


Why don't you just use PIL?
---------------------------

PIL is huge and has lots of dependencies, may be an overkill if you just want the dimensions. 
If you already have PIL installed, then sure, use it instead.

Usage
-----

Right now only for PNG, JPEG and GIF. Very untested, fork and send PRs.

    from get_image_size import image_size
    
    try:
        width, height = image_size('/path/to/image.ext')
    except UnknownImageFormat:
        width, height = -1, -1
        
