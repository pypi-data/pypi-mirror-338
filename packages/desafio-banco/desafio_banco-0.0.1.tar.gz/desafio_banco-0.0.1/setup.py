from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="desafio_banco",
    version="0.0.1",
    author="bruno_rodrigues",
    author_email="fidbruno@hotmail.com",
    description="Desafio Banco - Projeto de Python DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrunoRodri/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)