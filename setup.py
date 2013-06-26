from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='spanky.wizardPOC',
      version=version,
      description="Spanky: Wizard Proof of Concept",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='z3cforms wizard',
      author='Spanky',
      author_email='spanky@kapanka',
      url='https://github.com/spanktar/spanky.wizardPOC',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['spanky'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.z3cform',
          'plone.supermodel', 
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      #setup_requires=["PasteScript"],
      #paster_plugins=["ZopeSkel"],
      )
