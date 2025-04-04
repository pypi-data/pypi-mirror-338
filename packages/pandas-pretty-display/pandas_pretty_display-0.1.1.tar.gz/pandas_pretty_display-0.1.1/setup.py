from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pandas-pretty-display",
    version="0.1.1",
    author="Balaji",
    author_email="bala@python4u.in",
    description="A package to make pandas DataFrames display beautifully in Jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bala-srm/pandas-pretty-display-.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "ipython>=7.0.0",
        "pandas>=1.0.0"
    ],
)
