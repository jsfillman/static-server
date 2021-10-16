from setuptools import setup

setup(
    name='static-server',
    version='0.1',
    packages=['kbase-static-server'],
    url='https://github.com/jsfillman/static-server',
    license='',
    author='JS Fillman',
    author_email='jsfillman@lbl.gov',
    description='Simple Flask app to pull & serve static content',
    install_requires=[
        'datetime',
        'flask',
        'git',
        'os'
    ]
)
