from setuptools import setup, find_packages

setup(name='census-income',
versions = "0.0.1",
author = "dev mandloi",
author_email = "devmandloi37@gmail.com",
packages= find_packages(),
install_requires = ["pandas","numpy","flask"]
)