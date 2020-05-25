import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sr2vgi",
    version="0.0.1",
    author="Anderson Soares, Michel Chaves e José Fronza",
    author_email="andersonreis.geo@gmail.com",
    description="A package to vegetation indexes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andersonreisoares/sr2vgi/",
    packages=['sr2vgi'],
    install_requires=[
    'numpy',
    'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
) 