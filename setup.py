from setuptools import setup

VERSION = '0.2.0'

setup(
    name='get_image_size',
    url='https://github.com/scardine/image_size',
    version=VERSION,
    long_description=open('README.rst').read(),
    author='github.com/scardine',
    author_email=' ',
    py_modules=['get_image_size'],
    entry_points={
      'console_scripts': [
        'get_image_size = get_image_size:main',
        ],
    },
)
