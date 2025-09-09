from setuptools import setup, find_packages


setup(
    name="Initium",
    version="2.2",
    author="Aditya Prasetyo",
    description="Interface CLI for web development tools installation",
    packages=find_packages(),
    install_requires=[
        "rich",
        "pyfiglet",
    ],
    entry_points={
        "console_script": [
            "initium = initium.main:main",
        ],
    },
)
