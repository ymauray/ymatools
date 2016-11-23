"""yamtools : a set of tools for my personal needs.
"""

# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yamtools',

    version='0.1.0',

    description='yamtools : a set of tools for my personal needs.',
    long_description=long_description,

    url='https://github.com/ymauray/ymatools',

    author='The French Guy from Switzerland',
    author_email='yannick@frenchguy.ch',

    license='GPLv3+',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Podcast publishers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],

    keywords='python tools',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*'])
)
