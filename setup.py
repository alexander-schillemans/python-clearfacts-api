from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'python-clearfacts-api',         
  packages=['clearfacts', 'exactonline.models', 'exactonline.constants', 'exactonline.cache', 'exactonline.endpoints'],
  version = '0.1.0',
  license='GPL-3.0-or-later',
  description = 'Basic wrapper for the Clearfacts GraphQL API',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Alexander Schillemans',
  author_email = 'alexander.schillemans@hotmail.com',
  url = 'https://github.com/alexander-schillemans/python-clearfacts-api',
  download_url = 'https://github.com/alexander-schillemans/python-clearfacts-api/archive/refs/tags/0.1.0.tar.gz',
  keywords = ['clearfacts', 'clear', 'facts', 'api'],
  install_requires=[
          'requests',
          'oauthlib',
          'requests_oauthlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3.10',
  ],
)