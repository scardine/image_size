image_size
==========

Get image width and height given a file path using minimal dependencies (no need for PIL, libjpeg, libpng, etc).



usage
-----

Right now only for PNG, JPEG and GIF. Very untested, fork and send PRs.

    from get_image_size import image_size
    
    try:
        width, height = image_size('/path/to/image.ext')
    except UnknownImageFormat:
        width, height = -1, -1
        
