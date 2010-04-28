from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1.1'

install_requires = []

setup(name='django-immutablefield',
    version=version,
    description="A base class for Django to allow immutable fields on Models",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Database'
    ],
    keywords='django model fields immutable frozen',
    author='Rob Madole',
    author_email='robmadole@gmail.com',
    url='http://bitbucket.org/robmadole/django-immutablefield',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={}
)
