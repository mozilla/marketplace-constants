from setuptools import setup


setup(
    name='marketplace-constants',
    version='0.5.1',
    description='Standard constants for the marketplace',
    long_description=open('README.md').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    packages=[
        'mpconstants',
        'mpconstants/regions'
    ],
    url='https://github.com/andymckay/marketplace-constants',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ]
)
