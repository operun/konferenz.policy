from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='konferenz.policy',
      version=version,
      description="Konferenz Policy Package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Stefan Antonelli',
      author_email='stefan.antonelli@operun.de',
      url='http://svn.operun.de/svn/konferenz/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['konferenz'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )