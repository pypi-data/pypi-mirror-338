import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.8' 
PACKAGE_NAME = 'GlueTools' 
AUTHOR = 'Meloddy Guzmán Palma' 
AUTHOR_EMAIL = 'guzmanpalmamel@gmail.com' 
URL = 'https://github.com/yddolem' 

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Librería con funciones utilizadas recurrentemente por el Equipo BI' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') 
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
      'setuptools'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)