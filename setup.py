try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import aspirin 

SHORT = 'aspirin'

setup(
    name='aspirin',
    packages=[
        'aspirin'
    ],
    url='https://github.com/javiermas/dudewheresmyaspirin/',
    classifiers=(
        'Programming Language :: Python :: 3.6'
    ),
    description=SHORT,
    long_description=SHORT,
)
