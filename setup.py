#!/usr/bin/env python
from setuptools import setup, find_packages
from pupa import __version__

long_description = ''

setup(name='pupa',
      version=__version__,
      packages=find_packages(),
      author='James Turk',
      author_email='jturk@sunlightfoundation.com',
      license='BSD',
      url='http://github.com/opencivicdata/pupa/',
      description='scraping framework for muncipal data',
      long_description=long_description,
      platforms=['any'],
      entry_points='''[console_scripts]
pupa = pupa.cli.__main__:main''',
      install_requires=[
          #'Django==1.7.0',
          'dj_database_url==0.3.0',
          'opencivicdata-django>=0.7.0',
          'opencivicdata-divisions',
          'scrapelib>=0.10',
          'validictory>=1.0.0a2',
          'psycopg2',
          'pytz',
          'boto',
          #'kafka-python',  # Optional Kafka dep
      ],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.4",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
)
