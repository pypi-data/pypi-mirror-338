# setup.py

from setuptools import setup

import cfgr

setup(
    name="ucfgr",
    provides=["cfgr"],
    version=cfgr.VERSION,
    description="The universal config file manager for python",
    author="Harcic",
    author_email="harcic@outlook.com",
    url="https://github.com/HarcicYang/UConfigManager",
    packages=["cfgr", "cfgr.utils"],
    install_requires=["PyYAML"],
    include_package_data=True,
)
