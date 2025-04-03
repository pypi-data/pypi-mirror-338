from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Tech_Challenge_FIAP_Gabriel',
    version='1.0.3',
    packages=find_packages(),
    description='Teste de publicação no Pypi',
    author='Gabriel Siqueira de Lima',
    author_email='gabrielsiqueira61@hotmail.com',
    url='https://github.com/gabrielsiqueira97/tech-challenge-fiap',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
