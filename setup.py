"""
Flask-Bitcoind
-------------

Flask-Bitcoind initializes a Bitcoin JSON-RPC interface that can be used across
your app for communicating with a local or remote bitcoind node.
"""
from setuptools import setup


setup(
    name='Flask-Bitcoind',
    version='0.0.1',
    url='https://github.com/lightning-power-users/flask-bitcoind',
    license='MIT',
    author='Pierre Rochard',
    author_email='pierre@rochard.org',
    description='An Bitcoin JSON-RPC interface for Flask',
    long_description=__doc__,
    py_modules=['flask_bitcoind'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'python-bitcoinlib'
    ],
    keywords="bitcoind json rpc bitcoin flask",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
