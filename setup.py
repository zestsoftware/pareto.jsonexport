from setuptools import setup, find_packages
import os

version = '1.1.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open(os.path.join('docs', 'CONTRIBUTORS.txt')).read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='pareto.jsonexport',
      version=version,
      description="Export Zope/Plone objects to JSON.",
      long_description=long_description,
      # Get more strings from
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='json Plone export',
      author='Guido Wesdorp (Pareto) and Zest Software',
      author_email='guido.wesdorp@pareto.nl',
      url='http://zeelandia.com/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pareto', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'BeautifulSoup==3.2.1',
      ],
      extras_require={'test': ['plone.app.testing', 'unittest2']},
      test_suite='tests',
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
