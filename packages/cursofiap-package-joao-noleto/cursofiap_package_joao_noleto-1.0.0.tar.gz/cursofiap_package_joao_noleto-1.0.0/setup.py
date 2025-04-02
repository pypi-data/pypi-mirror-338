from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='cursofiap-package-joao-noleto',  # Nome único
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib cursofiap',
    author='João Pedro Noleto',
    author_email='jpnoleto1@gmail.com',
    url='https://github.com/tadrianonet/cursofiap',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)