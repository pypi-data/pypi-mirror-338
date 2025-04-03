from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='investimentpy-package',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib investimentpy',
    author='Marina Oliveira',
    author_email='marina.oliveira.lw@gmail.com',
    url='https://github.com/mari-oliv/investimentpy',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
