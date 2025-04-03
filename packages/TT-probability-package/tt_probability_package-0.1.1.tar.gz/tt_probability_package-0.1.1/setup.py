from setuptools import setup, find_packages
import os

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

long_description = ""

if os.path.exists("README.md"):
    with open("README.md", encoding="utf-8") as readme_file:
        long_description += readme_file.read() + "\n\n"

if os.path.exists("CHANGELOG.txt"):
    with open("CHANGELOG.txt", encoding="utf-8") as changelog_file:
        long_description += changelog_file.read()

setup(
    name='timothytewprobabilitylibrary',
    version='0.1.1',
    description='Basic probability library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',  
    author='Timothy Tew',
    author_email='tewtimothy@gmail.com',
    license='MIT', 
    classifiers=classifiers,
    keywords='probability', 
    packages=find_packages(),
    install_requires=[]
)