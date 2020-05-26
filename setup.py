from setuptools import setup

requirements = [emoji,random]

setup(name="dobble",
      version="0.1",
      description="card game dobble",
      url="",
      author="Richard Daly",
      author_email="richard.daly@ucdconnect.ie",
      licence="GPL3",
      packages=['dobble'],
      install_requires=requirements,
      entry_points={
        'console_scripts':['run_dobble=dobble.main:main']
        }
      )






