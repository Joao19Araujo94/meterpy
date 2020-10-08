# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='meterpy',
    version='0.4.0',
    description='JMeter API Test Builder & Processer',
    long_description=readme,
    author='Joao Miguel Araujo',
    author_email='joao19carrico94@gmail.com',
    url='https://github.com/Joao19Araujo94/meterpy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)