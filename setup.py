from setuptools import setup

setup(
   name='space_shooter',
   version='1.0',
   description='Pygame project for the Auburn University CPSC 4970 Python elective.',
   author='Jordan Gibson',
   author_email='jpg0041@auburn.edu',
   packages=['space_shooter'],  #same as name
   install_requires=['pygame'], #external packages as dependencies
)