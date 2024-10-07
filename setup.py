from setuptools import setup, find_packages

setup(
    name="seazen",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        'cycler'
    ],
    author="Raj Saha",
    author_email="raj@sage-labs.io",
    description="A custom theme for Seaborn and Matplotlib",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/seazen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
