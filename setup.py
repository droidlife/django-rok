from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rok',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Public url for your local web server.',
    long_description=README,
    author='Ankur Jain',
    author_email='ankurj630@gmail.com',
    url='https://github.com/droidlife/django-rok',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
          'paramiko>=2.4.1'
      ]
)
