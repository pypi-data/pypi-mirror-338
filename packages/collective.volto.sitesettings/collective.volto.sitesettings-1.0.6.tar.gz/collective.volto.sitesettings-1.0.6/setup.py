# -*- coding: utf-8 -*-
"""Installer for the collective.volto.sitesettings package."""

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
    name="collective.volto.sitesettings",
    version="1.0.6",
    description="Plone addon to allow to extend @site controlpanel",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="RedTurtle Technology",
    author_email="sviluppo@redturtle.it",
    url="https://github.com/collective/collective.volto.sitesettings",
    project_urls={
        "PyPI": "https://pypi.org/project/collective.volto.sitesettings/",
        "Source": "https://github.com/collective/collective.volto.sitesettings",
        "Tracker": "https://github.com/collective/collective.volto.sitesettings/issues",
        # 'Documentation': 'https://collective.volto.sitesettings.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.volto"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "setuptools",
        "Plone",
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
    update_locale = collective.volto.sitesettings.locales.update:update_locale
    """,
)
