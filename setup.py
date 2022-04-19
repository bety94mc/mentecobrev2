from setuptools import setup, find_packages

setup(
   name='mentecobre',
   python_requires='3.8',
   version='1.0',
   description='Herramienta para la traducción de la Coppermind',
   author='Sira',
   author_email='sira@cosmere.es',
   packages=find_packages(),
   scripts=['manage.py']
  
)