#  Drakkar-Software OctoBot-Channels
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
# from distutils.extension import Extension

from setuptools import dist
dist.Distribution().fetch_build_eggs(['Cython>=0.29.14'])

try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
except ImportError:
    # create closure for deferred import
    def cythonize(*args, **kwargs):
        from Cython.Build import cythonize
        return cythonize(*args, **kwargs)

    def build_ext(*args, **kwargs):
        from Cython.Distutils import build_ext
        return build_ext(*args, **kwargs)

from setuptools import find_packages
from setuptools import setup, Extension

PACKAGES = find_packages(exclude=["tests"])

packages_list = ["list_operations.filtering.lists_filtering_with_list_as_values"]

ext_modules = [
    Extension(package, [f"{package.replace('.', '/')}.py"])
    for package in packages_list]

setup(
    name="OctoBot-Benchmarks",
    version="1.0.0",
    url='https://github.com/Drakkar-Software/OctoBot-Benchmarks',
    license='LGPL-3.0',
    author='Drakkar-Software',
    author_email='drakkar-software@protonmail.com',
    description='OctoBot benchmarks',
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(ext_modules)
)
