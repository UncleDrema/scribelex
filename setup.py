from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scribelex",
    version="1.0.6",
    author="UncleDrema",
    author_email="missl.wipiece@gmail.com",
    description="Scribelex is a lightweight Python library for building parser combinators.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["parser", "parsing", "combinator", "library", "Python", "structured data", "grammar", "syntax", "parsing toolkit"],
    url="https://github.com/UncleDrema/scribelex",
    packages=find_packages("src"),
    package_dir={"": "src"},
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)