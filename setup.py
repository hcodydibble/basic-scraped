from setuptools import setup

requires = [
    'requests',
    'beautifulsoup4'
]

tests_require = [
    'pytest',
    'pytest-cov',
    'tox'
]

setup(
    name='web_scraper',
    version='0.0',
    description='A basic web scraper for the King County Health Inspection API',
    author='H. Cody Dibble',
    author_email='hcodydibble@gmail.com',
    url='',
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            '',
        ],
    },
)
