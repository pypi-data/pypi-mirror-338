from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()
setup(
    name='cisco_discovery',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.2.3',
        'openpyxl>=3.1.5',
        'genie>=25.3',
        'pyats>=25.3',
        'netmiko>=4.5.0',
        'dotenv>=0.9.9',
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)