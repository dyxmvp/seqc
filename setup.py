import os
import sys
import shutil
from subprocess import call, check_output
from setuptools import setup
from warnings import warn

if sys.version_info.major != 3:
    raise RuntimeError('SEQC requires Python 3')
if sys.version_info.minor < 5:
    warn('Multiprocessing analysis methods may not function on Python versions < 3.5')

# install phenograph
call(['pip3', 'install', 'git+https://github.com/jacoblevine/phenograph.git'])

# get version
with open('src/seqc/version.py') as f:
    exec(f.read())

setup(name='seqc',
      version=__version__,  # read in from the exec of version.py; ignore error
      description='Single Cell Sequencing Processing and QC Suite',
      author='Ambrose J. Carr',
      author_email='mail@ambrosejcarr.com',
      package_dir={'': 'src'},
      packages=['seqc', 'seqc.sequence', 'seqc.alignment', 'seqc.core'],
      install_requires=[
          'numpy>=1.10.0',
          'bhtsne',
          'wikipedia',
          'awscli',
          'cython>0.14',
          'numexpr>=2.4',
          'pandas>=0.18.1',
          'paramiko>=2.0.2',
          'regex',
          'requests',
          'nose2',
          'scipy>=0.14.0',
          'boto3',
          'intervaltree',
          'matplotlib',
          'tinydb',
          'tables',
          'fastcluster',
          'statsmodels',
          'ecdsa',
          'dill',
          'pycrypto',
          'scikit_learn>=0.17'],
      scripts=['src/seqc/core/SEQC.py'],
      extras_require={
          'GSEA_XML': ['html5lib', 'lxml', 'BeautifulSoup4'],
      }
      )

# look for star
if not shutil.which('STAR'):
    warn('SEQC: STAR is not installed. SEQC will not be able to align files.')
