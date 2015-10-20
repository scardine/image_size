
import codecs
from setuptools import setup

VERSION = '0.2.0'


def read_long_description():
    long_desc = []
    with codecs.open('README.rst', 'r', 'utf8') as longdesc:
        long_desc.append(longdesc.read())
    with codecs.open('HISTORY.rst', 'r', 'utf8') as history:
        long_desc.append(history.read())
    return u'\n\n'.join(long_desc)

LONG_DESCRIPTION = read_long_description()

setup(
    name='get_image_size',
    url='https://github.com/scardine/image_size',
    version=VERSION,
    long_description=LONG_DESCRIPTION,
    author='github.com/scardine',
    author_email=' ',
    license='MIT',
    py_modules=['get_image_size'],
    entry_points={
        'console_scripts': [
            'get-image-size = get_image_size:main',
            ],
    },
)
