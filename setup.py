from setuptools import setup


setup(
    name='marketplace-constants',
    version='0.1.1',
    description='Standard constants for the marketplace',
    long_description=open('README.txt').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    packages=['mpconstants'],
    url='https://github.com/andymckay/marketplace-constants',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ]
)
