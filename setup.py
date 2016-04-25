#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='gh_org',
    description="GitHub Organization Management",
    license='Apache 2.0',
    author='David M Noriega',
    author_email='davidmnoriega@gmail.com',
    version='0.1',
    packages=['gh_org'],
    entry_points={
        'console_scripts': ['gh_org=gh_org.cli:main']},
    install_requires=['ldap3'],
    )
