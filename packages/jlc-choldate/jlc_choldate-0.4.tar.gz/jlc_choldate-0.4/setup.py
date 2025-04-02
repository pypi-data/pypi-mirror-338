from Cython.Build import cythonize
from distutils.extension import Extension
from setuptools import setup

import numpy

setup(
    ext_modules=cythonize(
        [
            Extension(
                "choldate._choldate",
                ["choldate/_choldate.pyx"],
                include_dirs=[numpy.get_include()],
            )
        ]
    ),
)
