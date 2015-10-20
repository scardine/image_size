from setuptools import setup

setup(
    name='get_image_size',
    py_modules=['get_image_size'],
    url='https://github.com/scardine/image_size',
    entry_points={
      'console_scripts': [
        'get_image_size = get_image_size:main',
        ],
    },
    long_description=open('README.rst').read(),
)
