from setuptools import setup, find_packages

setup(
    name='simplypy',  # Name of your package
    version='0.2.0',  # Version number
    description='My first Python library',  # Short description of your package
    long_description=open('README.md').read(),  # Long description from README file
    long_description_content_type='text/markdown',  # Type of content in the long description
    author='Hrithik Sagar',  # Author name
    author_email='hrithiksagar36@gmail.com',  # Author email
    url='https://github.com/hrithiksagar/simplypy',  # URL to the project's homepage or repository
    packages=find_packages(include=['simplypy', 'simplypy.*']),  # Packages to include
    install_requires=[
        # List of dependencies required for your package to run
        'pandas>=1.0.0',
        'pyyaml>=5.3'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    # extras_require={
    #     'dev': ['pytest>=4.4.1', 'flake8'],  # Additional packages for development
    #     'docs': ['sphinx']
    # },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',  # Minimum version of Python required
    license='Apache 2',  # License type
    # keywords='example library setup.py',  # Keywords for your package
    project_urls={
        'Bug Reports': 'https://github.com/hrithiksagar/simplypy/issues',
        'Source': 'https://github.com/hrithiksagar/simplypy/',
    },
)