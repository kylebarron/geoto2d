#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()
    requirements = [x[:-1] for x in requirements]

setup_requirements = ['setuptools >= 38.6.0', 'twine >= 1.11.0']

# yapf: disable
setup(
    author="Kyle Barron",
    author_email='kylebarron2@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI script to remove third dimension from GeoJSON features",
    entry_points={
        'console_scripts': [
            'geoto2d=geoto2d.geoto2d:geoto2d',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='geoto2d',
    name='geoto2d',
    packages=find_packages(include=['geoto2d', 'geoto2d.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    url='https://github.com/kylebarron/geoto2d',
    version='0.1.0',
    zip_safe=False,
)