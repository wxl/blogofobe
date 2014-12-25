# -*- coding: utf-8 -*-
import sys
from setuptools import setup
import blogofobe


py_version = sys.version_info[:2]
PY3 = py_version[0] == 3
PY26 = py_version == (2, 6)
if PY3:
    if py_version < (3, 2):
        raise RuntimeError(
            'On Python 3, blogofobe requires Python 3.2 or later')
else:
    if py_version < (2, 6):
        raise RuntimeError(
            'On Python 2, blogofobe requires Python 2.6 or later')

with open('README.md', 'rt') as readme:
    long_description = readme.read()

install_requires = [
    'docutils',
    'Jinja2',
    'Mako',
    'Markdown',
    'MarkupSafe',
    'Pygments',
    'pytz',
    'PyYAML',
    'six',
    'Unidecode',
]
dependency_links = []
if PY3:
    install_requires.append('textile==2.1.4-py3k')
    dependency_links = [
        'http://github.com/EnigmaCurry/textile-py3k/tarball/2.1.4'
        '#egg=textile-2.1.4-py3k']
else:
    install_requires.append('textile')
if PY26:
    install_requires.append('argparse')

classifiers = [
    'Programming Language :: Python :: {0}'.format(py_version)
    for py_version in ['2', '2.6', '2.7', '3', '3.2']]
classifiers.extend([
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: Implementation :: CPython',
    'Environment :: Console',
    'Natural Language :: English',
])

setup(
    name="blogofobe",
    version=blogofobe.__version__,
    description="A static website compiler and blog engine",
    long_description=long_description,
    author=blogofobe.__author__,
    author_email="wxl@polka.bike",
    url="http://github.com/wxl/blogofobe",
    license="MIT",
    classifiers=classifiers,
    packages=["blogofobe"],
    install_requires=install_requires,
    dependency_links=dependency_links,
    zip_safe=False,
    entry_points={
        'console_scripts': ['blogofobe = blogofobe.main:main']},
)
