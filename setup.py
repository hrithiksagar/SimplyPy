
from setuptools import find_packages, setup

setup(
    name='simplypy',
    packages=find_packages(include=['simplypy']),
    version='0.1.0',
    description='My first Python library',
    author='Hrithik_Sagar',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)