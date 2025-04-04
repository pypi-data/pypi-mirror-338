from setuptools import setup, find_packages # type: ignore
setup(
   name='dereberus',
   version='1.5',
   packages=find_packages(),
   install_requires=[
      'click',
   ],
   entry_points='''
      [console_scripts]
      dereberus=cli_bundle.cli:dereberus_commands
      ''',
)