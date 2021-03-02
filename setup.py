from setuptools import setup
from distutils.core import Extension

# Python 2.6 will error exiting nosetests via multiprocessing without this
# import, as arbitrary as it seems.
#
import multiprocessing  # noqa

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='pybutton',
    version='4.0.0',
    description='Client for the Button API',
    long_description=long_description,
    author='Button',
    author_email='support@usebutton.com',
    url='https://www.usebutton.com/developers/api-reference/',
    packages=['pybutton', 'pybutton/resources'],
    include_package_data=False,
    license='MIT',
    test_suite='nose.collector',
    tests_require=['nose', 'mock', "flake8-quotes==2.1.0"],
    zip_safe=True,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    ext_modules = [Extension(name = "pybutton.resources.private_audience.bitarray._bitarray",
                             sources = ["pybutton/resources/private_audience/bitarray/_bitarray.c"]),
                   Extension(name = "pybutton.resources.private_audience.bitarray._util",
                             sources = ["pybutton/resources/private_audience/bitarray/_util.c"])],
)
