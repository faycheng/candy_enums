# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

README = """# candy_enums
"""


setup(
    name='candy_enums',
    version='0.1.1',
    description='useful enums',
    long_description=README,
    author='程飞',
    url='https://github.com/faycheng/candy_enums.git',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    entry_points={
        'console_scripts': [],
    },
    zip_safe=True,
    license='MIT License',
    classifiers=['development status :: 1 - planning', 'topic :: software development :: libraries', 'programming language :: python :: 3 :: only', 'environment :: macos x']
)