#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        get_image_size
# Purpose:     extract image dimensions given a file path
#
# Author:      Paulo Scardine (based on code from Emmanuel VAÏSSE)
#
# Created:     26/09/2013
# Copyright:   (c) Paulo Scardine 2013
# Licence:     MIT
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import os
import struct

FILE_UNKNOWN = "Sorry, don't know how to get size for this file."

class UnknownImageFormat(Exception):
    pass

def get_image_size(file_path):
    """
    Return (width, height) for a given img file content - no external
    dependencies except the os and struct builtin modules
    """
    size = os.path.getsize(file_path)

    # be explicit with open arguments - we need binary mode
    with open(file_path, "rb") as input:
        height = -1
        width = -1
        data = input.read(26)
        msg = " raised while trying to decode as JPEG."

        if (size >= 10) and data[:6] in ('GIF87a', 'GIF89a'):
            # GIFs
            w, h = struct.unpack("<HH", data[6:10])
            width = int(w)
            height = int(h)
        elif ((size >= 24) and data.startswith('\211PNG\r\n\032\n')
              and (data[12:16] == 'IHDR')):
            # PNGs
            w, h = struct.unpack(">LL", data[16:24])
            width = int(w)
            height = int(h)
        elif (size >= 16) and data.startswith('\211PNG\r\n\032\n'):
            # older PNGs
            w, h = struct.unpack(">LL", data[8:16])
            width = int(w)
            height = int(h)
        elif (size >= 2) and data.startswith('\377\330'):
            # JPEG
            input.seek(0)
            input.read(2)
            b = input.read(1)
            try:
                while (b and ord(b) != 0xDA):
                    while (ord(b) != 0xFF): b = input.read(1)
                    while (ord(b) == 0xFF): b = input.read(1)
                    if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                        input.read(3)
                        h, w = struct.unpack(">HH", input.read(4))
                        break
                    else:
                        input.read(int(struct.unpack(">H", input.read(2))[0])-2)
                    b = input.read(1)
                width = int(w)
                height = int(h)
            except struct.error:
                raise UnknownImageFormat("StructError" + msg)
            except ValueError:
                raise UnknownImageFormat("ValueError" + msg)
            except Exception as e:
                raise UnknownImageFormat(e.__class__.__name__ + msg)
        elif (size >= 26) and data.startswith('BM'):
            # BMP
            headersize = struct.unpack("<I", data[14:18])[0]
            if headersize == 12:
                w, h = struct.unpack("<HH", data[18:22])
                width = int(w)
                height = int(h)
            elif headersize >= 40:
                w, h = struct.unpack("<ii", data[18:26])
                width = int(w)
                height = abs(int(h)) # as h is negative when stored upside down
            else:
                raise UnknownImageFormat("Unkown DIB header size:" + str(headersize))
        elif (size >= 8) and data[:4] in ("II\052\000", "MM\000\052"):
            # Standard TIFF, big- or little-endian
            # BigTIFF and other different but TIFF-like formats are not supported currently
            byteOrder = data[:2]
            boChar = ">" if byteOrder == "MM" else "<"
            ifdOffset = struct.unpack(boChar + "L", data[4:8])[0]
            try:
                countSize = 2
                input.seek(ifdOffset)
                ec = input.read(countSize)
                ifdEntryCount = struct.unpack(boChar + "H", ec)[0]
                ifdEntrySize = 12 # 2 bytes: TagId + 2 bytes: type + 4 bytes: count of values + 4 bytes: value offset
                for i in range(ifdEntryCount):
                   entryOffset = ifdOffset + countSize + i * ifdEntrySize
                   input.seek(entryOffset)
                   tag = input.read(2)
                   tag = struct.unpack(boChar + "H", tag)[0]
                   if(tag == 256):
                       input.seek(entryOffset + 8)
                       w = input.read(2) # assuming SHORT atm, i.e. only imgs with max resolution of 64k x 64k supported
                       width = int(struct.unpack(boChar + "H", w)[0])
                   elif(tag == 257):
                       input.seek(entryOffset + 8)
                       h = input.read(2) # assuming SHORT atm, i.e. only imgs with max resolution of 64k x 64k supported
                       height = int(struct.unpack(boChar + "H", h)[0])
                   if width > -1 and height > -1:
                       break
            except Exception as e:
                raise UnknownImageFormat(str(e))
        elif size >= 2:
        	#see http://en.wikipedia.org/wiki/ICO_(file_format)
        	input.seek(0)
        	reserved = input.read(2)
        	if 0 != struct.unpack("<H", reserved )[0]:
        		raise UnknownImageFormat(FILE_UNKNOWN)
        	format = input.read(2)
        	assert 1 == struct.unpack("<H", format)[0]
        	num = input.read(2)
        	num = struct.unpack("<H", num)[0]
        	if num > 1:
        		import warnings
        		warnings.warn("ICO File contains more than one image")
        	#http://msdn.microsoft.com/en-us/library/ms997538.aspx
        	w = input.read(1)
        	h = input.read(1)
        	width = ord(w)
        	height = ord(h)
        else:
            raise UnknownImageFormat(FILE_UNKNOWN)

    return width, height

