# -*- coding: utf-8 -*-
"""Installer for the rer.immersivereader package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="rer.immersivereader",
    version="0.2.0",
    description="Plone integration for Microsoft's Immersive Reader",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="RedTurtle Technology",
    author_email="sviluppo@redturtle.it",
    url="https://github.com/collective/rer.immersivereader",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/rer.immersivereader",
        "Source": "https://github.com/collective/rer.immersivereader",
        "Tracker": "https://github.com/collective/rer.immersivereader/issues",
        # 'Documentation': 'https://rer.immersivereader.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["rer"],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False,
    install_requires=[
        "setuptools",
        "plone.restapi",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.restapi[test]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = rer.immersivereader.locales.update:update_locale
    """,
)
