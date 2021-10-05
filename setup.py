# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from devenv import VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="devenv",
    version=VERSION,
    author="sudo-julia",
    author_email="jlearning AT tuta DOT io",
    description="Automate the creation of development environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudo-julia/devenv",
    packages=find_packages(),
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    keywords="development automation",
    install_requires=["appdirs>=1.4.4"],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["devenv = devenv.devenv:main"],
    },
)
