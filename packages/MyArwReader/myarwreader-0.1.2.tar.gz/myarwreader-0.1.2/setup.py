from setuptools import setup, find_packages

# Read the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MyArwReader",
    version="0.1.2",  # updated for get_tags
    author="ARWEnthusiast",
    description="A lightweight package to read metadata from Sony .ARW files",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Tell PyPI it's Markdown
    packages=find_packages(),
    install_requires=["pyexiftool"],
    python_requires=">=3.6",
    license="MIT",
)