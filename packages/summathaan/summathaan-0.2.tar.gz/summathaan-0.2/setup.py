from setuptools import setup, find_packages

setup(
    name='summathaan',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts' : [
            'summathaan = summathaan:hello',
        ],
    },
)