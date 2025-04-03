from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='teste_fiap-package',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib teste_fiap',
    author='Miler Azevedo',
    author_email='estudos.miler@gmail.com',
    url='https://github.com/milerazevedo0/teste_fiap',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
