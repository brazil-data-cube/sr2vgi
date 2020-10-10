import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sr2vgi",
    version="0.0.2",
    author="Brazil Data Cube Team",
    author_email="brazildatacube@dpi.inpe.br",
    description="A package to vegetation indexes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brazil-data-cube/sr2vgi/",
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