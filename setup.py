from setuptools import setup

setup(name='Cart',
      version='1.0',
      py_modules=['cart'],
      install_requires=['Click','pandas','pyfiglet'],
      entry_points='''
      [console_scripts]
      cart=cart:cart
      ''',

      )