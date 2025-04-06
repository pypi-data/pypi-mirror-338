from setuptools import setup, find_packages

setup(
    name='summathaan',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        "pyttsx3"
    ],
    entry_points={
        'console_scripts' : [
            'hi = summathaan:hello',
            'hello = summathaan:hello',
        ],
    },
)