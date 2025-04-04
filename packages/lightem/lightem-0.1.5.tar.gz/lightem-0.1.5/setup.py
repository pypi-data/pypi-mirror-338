from setuptools import setup, find_packages
from lightem import __version__ as version
from lightem import __author__ as author
from lightem import __url__ as url
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

# pede permissão de adm pra apagar as pastas build, dist e lightem.egg-info
os.system("rmdir /S /Q build")
os.system("rmdir /S /Q dist")
os.system("rmdir /S /Q lightem.egg-info")

setup(
    name="lightem",
    version=version,
    description="A light-weight python package for multi-table entity matching.",
    packages=find_packages(),  # Ajuste aqui
    package_dir={},  # Ajuste para o diretório 'lightem'
    include_package_data=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email="<pedromendicino25@gmail.com>",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "gensim",
        "sentence-transformers",
    ],
    extras_require={
        "dev": ["twine>=6.1.0",],
    },
    python_requires='>=3.10',
)
