from setuptools import setup

# Python 2.6 will error exiting nosetests via multiprocessing without this
# import, as arbitrary as it seems.
#
import multiprocessing # noqa

from pybutton import VERSION

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='pybutton',
    version=VERSION,
    description='Client for the Button API',
    long_description=long_description,
    author='Button',
    author_email='support@usebutton.com',
    url='https://www.usebutton.com/developers/api-reference/',
    packages=['pybutton', 'pybutton/resources'],
    include_package_data=False,
    license='MIT',
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
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
    ]
)
