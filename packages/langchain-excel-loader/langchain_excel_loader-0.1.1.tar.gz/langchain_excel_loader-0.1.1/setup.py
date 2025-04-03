from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="langchain_excel_loader",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "openpyxl>=3.1.2",
        "langchain-core>=0.3.1",
        "langchain-community>=0.3.1",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)