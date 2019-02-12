#!/usr/bin/env python
"""pyang3 setup module."""

from pathlib import Path

from setuptools import find_packages, setup


PROJECT_HOME = "https://github.com/cmlccie/pyang/tree/pyang3"

PACKAGE_NAME = "pyang3"

PACKAGE_KEYWORDS = [
    "yang",
    "yin",
    "validator",
]

PACKAGE_CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Telecommunications Industry",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
]

INSTALLATION_REQUIREMENTS = [
    "lxml",
    "click",
]


project_root = Path(__file__).parent


# Get package metadata
metadata = {"__name__": PACKAGE_NAME}
with open(project_root/PACKAGE_NAME/"__init__.py", encoding="utf-8") as f:
    exec(f.read(), metadata)


# Get the long description from the project"s README file
with open(project_root/"README.md", encoding="utf-8") as f:
    long_description = f.read()
    long_description_content_type = "text/markdown"


# Locate data files
modules_iana = [str(f) for f in project_root.glob("modules/iana/*.yang")]
modules_ietf = [str(f) for f in project_root.glob("modules/ietf/*.yang")]
xslt = [str(f) for f in project_root.glob("xslt/*.xsl")]
schema = [str(f) for f in project_root.glob("schema/*.rng")]
images = [str(f) for f in project_root.glob("tools/images/*")]
man1 = [str(f) for f in project_root.glob("man/man1/*.1")]
data_files = [
    ("share/man/man1", man1),
    ("share/yang/modules/iana", modules_iana),
    ("share/yang/modules/ietf", modules_ietf),
    ("share/yang/xslt", xslt),
    ("share/yang/images", images),
    ("share/yang/schema", schema),
    ("etc/bash_completion.d", ["etc/bash_completion.d/pyang"]),
]


setup(
    name=PACKAGE_NAME,
    description=metadata.get("__description__", ""),
    version=metadata.get("__version__", ""),
    author=metadata.get("__author__", ""),
    author_email=metadata.get("__author_email__", ""),
    license=metadata.get("__license__", ""),
    url=PROJECT_HOME,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    install_requires=INSTALLATION_REQUIREMENTS,
    classifiers=PACKAGE_CLASSIFIERS,
    keywords=" ".join(PACKAGE_KEYWORDS),
    packages=find_packages(include=[PACKAGE_NAME, PACKAGE_NAME + '.*']),
    data_files=data_files,
)
