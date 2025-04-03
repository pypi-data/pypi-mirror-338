from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='aula3_curso_fiap-package',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib aula3_curso_fiap',
    author='seu nome',
    author_email='seu.email@example.com',
    url='https://github.com/tadrianonet/aula3_curso_fiap',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
