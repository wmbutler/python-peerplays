#!/usr/bin/env python

import codecs

from setuptools import setup
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))

VERSION = '0.0.3'

setup(
    name='peerplays',
    version=VERSION,
    description='Python library for PEERPLAYS',
    long_description=open('README.md').read(),
    download_url='https://github.com/xeroc/python-peerplays/tarball/' + VERSION,
    author='Fabian Schuh',
    author_email='Fabian@chainsquad.com',
    maintainer='Fabian Schuh',
    maintainer_email='Fabian@chainsquad.com',
    url='https://bitbucket.org/peerplaysblockchain/peerplays-python',
    keywords=['peerplays', 'library', 'api', 'rpc'],
    packages=[
        "peerplays",
        "peerplays.cli",
        "peerplaysapi",
        "peerplaysbase",
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Games/Entertainment',
    ],
    entry_points={
        'console_scripts': [
            'peerplays = peerplays.cli.cli:main',
        ],
    },
    install_requires=[
        "graphenelib>=0.5.0",
        "scrypt",
        "appdirs",
        "pycrypto",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
)
