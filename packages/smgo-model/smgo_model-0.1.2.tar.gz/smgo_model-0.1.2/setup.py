from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='smgo_model',
    version='v0.1.2',
    packages=['model'],
    description='Test de librería pip',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Vanda Dev',
    author_email='kevins.villatoro@vanda.cl',
    url='https://github.com/SmartGO-Inc/smartgo-model-libreria.git'
)
