from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='primeiraapi-package',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib primeiraapi',
    author='Yuri Fernandes',
    author_email='yurifernandespreto@gmail.com',
    url='https://github.com/Yuriferr/Fase-1-PosTech-IA/tree/Fundamentos-de-Inteligência-Artificial/aula03/primeiraapi',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
