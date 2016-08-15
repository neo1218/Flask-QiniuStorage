#!/usr/bin/env python

from setuptools import setup


setup(
    name='Flask-Zero',
    version='0.9.5',
    url='https://github.com/neo1218/Flask-Zero',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='Qiniu Storage for Flask',
    long_description='Qiniu Storage for Flask. Fork from https://github.com/csuzhangxc/Flask-QiniuStorage',
    py_modules=['flask_zero'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    keywords='qiniu for flask',
    package_data={'': ['LICENSE']},
    install_requires=[
        'setuptools',
        'Flask',
        'qiniu'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
