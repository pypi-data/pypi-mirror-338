from setuptools import setup, find_packages

setup(
    name='kamusrejang_cli',
    version='0.2',
    packages=find_packages(),
    install_requires=['requests', 'termcolor'],
    entry_points={
        'console_scripts': [
        'kamusrejang_cli = kamusrejang_cli.main:main',
        ],
    },
)

