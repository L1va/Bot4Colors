from setuptools import setup, find_packages


setup(
    name='bot',
    version='0.0.1',
    author='GomZik',
    author_email='gomzik000@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask==0.11',
        'gunicorn==19.6.0'
    ])
