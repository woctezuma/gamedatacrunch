from distutils.core import setup

# noinspection PyUnresolvedReferences
import setuptools

setup(
    name='gamedatacrunch',
    packages=['gamedatacrunch'],
    install_requires=[
        'requests',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    version='0.0.1',
    description='GameDataCrunch API on PyPI',
    long_description='gdc: an API for GameDataCrunch, written in Python 3.',
    long_description_content_type='text/markdown',
    author='Wok',
    author_email='wok@tuta.io',
    url='https://github.com/woctezuma/gamedatacrunch',
    download_url='https://github.com/woctezuma/gamedatacrunch/archive/0.0.1.tar.gz',
    keywords=['steam', 'gamedatacrunch', 'api'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)


