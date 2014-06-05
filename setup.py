import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pyreq",
    version="1.0.0",
    url='http://github.com/fcabaud/pyreq',
    license='Apache 2.0',
    description="Requirement collection & management",
    long_description=read('README.md'),
    author='Frederic Cabaud',
    author_email='fcabaud@gmail.com',
    maintainer='Arun K. R.',
    maintainer_email='the1.arun@gmail.com',
    packages=['pyReq'],
    install_requires=['openpyxl', 'pdfminer3k'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python  :: 3',
        'Topic :: Office/Business',
    ],
    scripts=[
        'bin/json2testlinkCsv',
        'bin/json2xlsx',
        'bin/pdf2json',
        'bin/pythonFilter',
        'xlsx2json'
    ]
)
