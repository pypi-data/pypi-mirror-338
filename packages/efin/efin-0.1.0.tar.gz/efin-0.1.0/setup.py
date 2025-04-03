from setuptools import setup, find_packages

setup(
    name="efin",
    version="0.1.0",
    author="Ethan Beirne",
    author_email="ethan.g.beirne@gmail.com",
    description="A Python library for financial valuation including DCF calculations.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/efin",  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        "yfinance",  # Required for fetching financial data
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
