from setuptools import setup, find_packages
import os

setup(name = 'steamer',
      version = '0.0.1',
      description = 'Steamer',
      #long_description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
      author = "Gustavo Maia Neto (Guto Maia)", author_email = "guto@guto.net",
      license = "GPL3",
      packages = find_packages(exclude=["*.tests", "*.tests.*", "examples"]),
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Topic :: Games/Entertainment',
        ],
      url = 'http://github.com/gutomaia/steamer-py/',
)