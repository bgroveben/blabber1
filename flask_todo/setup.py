from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_todo',
    version='0.0',
    description='Another to-do list built with Flask',
    author='bgroveben',
    author_email='bgroveben@gmail.com',
    keywords='python flask web',
    packages=find_packages(),
    include-package_data=True,
    install_requires=requires,
)
