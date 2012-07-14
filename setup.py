from distutils.core import setup, Command
from setuptools.command.test import test as TestCommand

class PyTest(Command):
    user_options = []

    initialize_options = lambda s: None
    finalize_options = lambda s: None

    def run(self):
        import sys
        import os
        import subprocess
        os.environ['PYTHONPATH'] = '.'
        errno = subprocess.call(['py.test', '--cov', 'tbot'])
        raise SystemExit(errno)

setup(
    name='tbot',
    version='0.1dev',
    packages=['tbot'],
    license='3-Clause BSD',
    author='Corey Richardson',
    author_email='python@octayn.net',
    url='github.com/cmr/tbot',
    long_description=open('README.rst').read(),
    tests_require=['pytest', 'mock', 'pytest-cov'],
    cmdclass = dict(test=PyTest),
)
