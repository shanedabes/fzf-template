#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Shane Donohoe",
    author_email='shane@donohoe.cc',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Template files using yaml config and an fzf selector",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            'fzf_template = fzf_template.fzf_template:main'
        ]
    },
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fzf_template',
    name='fzf_template',
    packages=find_packages(include=['fzf_template']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/shanedabes/fzf_template',
    version='0.1.0',
    zip_safe=False,
)
