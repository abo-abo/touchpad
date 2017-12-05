#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='touchpad',
    version='0.1.3',
    description='Toggle touchpad on/off',
    packages=find_packages(),
    url='https://github.com/abo-abo/touchpad-toggle',
    author='Oleh Krehel',
    author_email='ohwoeowho@gmail.com',
    license='GPLv3+',
    keywords='touchpad',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    install_requires=["pycook"],
    entry_points={'console_scripts': ['tt=touchpad.touchpad:main']}
)
