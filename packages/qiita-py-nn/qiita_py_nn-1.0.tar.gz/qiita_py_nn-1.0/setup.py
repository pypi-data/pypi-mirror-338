''' Wrapper for Qiita API v2

created by @nekoniii3

fork from https://github.com/petitviolet/qiita_py
'''

import os
from setuptools import setup, find_packages
from qiita_py_nn import (__author__, __license__, __version__, __name__)

long_desc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name=__name__,
    author=__author__,
    version=__version__,
    license=__license__,
    author_email='nekonii3.dev@gmail.com',
    url='https://github.com/nekoniii3/qiita_py_nn',
    description='Python Wrapper for Qiita API v2',
    long_description=long_desc,
    platforms='any',
    packages=find_packages(),
    install_requires=['pyyaml', 'requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
