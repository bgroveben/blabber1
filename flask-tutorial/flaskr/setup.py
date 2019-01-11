from setuptools import setup, find_packages

# https://packaging.python.org/tutorials/packaging-projects/

setup(
    name='flaskr',
    version='0.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
