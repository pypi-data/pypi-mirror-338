from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='my_investimento-package',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib my_investimento',
    author='Marcelo N Morais',
    author_email='marcnobremorais@gmail.com',
    url='https://github.com/tadrianonet/my_investimento',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
