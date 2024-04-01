"""Setup file for distribution artifacts."""
from __future__ import print_function

from os import path
import sys

from setuptools import setup


(major, minor) = (sys.version_info.major, sys.version_info.minor)
if major != 3 or minor < 7:
    print('firebase_admin requires python >= 3.7', file=sys.stderr)
    sys.exit(1)

# Read in the package metadata per recommendations from:
# https://packaging.python.org/guides/single-sourcing-package-version/
about_path = path.join(path.dirname(path.abspath(__file__)), 'firedrop_cli', '__about__.py')
about = {}
with open(about_path) as fp:
    exec(fp.read(), about)  # pylint: disable=exec-used


long_description = ('CLI tool to trigger various behavours related to the Firedrop iOS app.')
install_requires = [
    'requests>=2.31.0',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description='Firedrop CLI',
    long_description=long_description,
    url=about['__url__'],
    scripts=['bin/firedrop-cli'],
    project_urls={
        'Release Notes': '',
        'Source': '',
    },
    author=about['__author__'],
    license=about['__license__'],
    keywords='firedrop cli',
    install_requires=install_requires,
    packages=['firedrop_cli'],
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)