import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='flaskr',
    version='1.0.0',
    url='https://github.com/bgroveben/flask_apps',
    license='BSD',
    description='The basic blog app built in the Flask tutorial',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage'
        ],
    },
)
