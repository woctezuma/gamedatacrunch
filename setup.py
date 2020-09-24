import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gamedatacrunch',
    version='0.0.2',
    author='Wok',
    author_email='wok@tuta.io',
    description='GameDataCrunch API on PyPI',
    keywords=['steam', 'gamedatacrunch', 'api'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/woctezuma/gamedatacrunch',
    download_url='https://github.com/woctezuma/gamedatacrunch/archive/0.0.2.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Games/Entertainment',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
