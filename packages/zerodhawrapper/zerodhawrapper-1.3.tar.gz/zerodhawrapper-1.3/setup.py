from setuptools import setup, find_packages

setup(
    name="zerodhawrapper",
    version="1.3",  # Incrementing from current version 1.2
    packages=find_packages(),
    install_requires=[
        "kiteconnect",
        "pandas",
        "furl",
        "nsetools",
        "prettytable",
        "pyotp",
        "webdriver-manager",
        "selenium"
    ],
    author="Kunal Agarwal",
    author_email="kunal.95a@gmail.com",
    description="A Python wrapper for the Zerodha API that simplifies interaction with Zerodha's trading platform",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kunalAgarwal35/zerodha_wrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 