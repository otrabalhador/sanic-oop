import re

from setuptools import setup


def version():
    version_file_name = "sanic_oop/__init__.py"
    with open(version_file_name, 'rt') as version_file:
        version_file_content = version_file.read()

        version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
        match = re.search(version_regex, version_file_content, re.M)
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Unable to find version string in %s." % (version_file_name,))


setup(name='sanic-oop',
      version=version(),
      author='Eryk Humberto Oliveira Alves',
      author_email='erykwho@gmail.com',
      url='https://github.com/otrabalhador/sanic-oop/',
      install_requires=["sanic==0.7.0",
                        "sanic-cors==0.9.3",
                        "sanic-openapi==0.4.0"],
      packages=[
          'sanic_oop',
          'sanic_oop/blueprint',
          'sanic_oop/error_handler',
          'sanic_oop/listeners',
          'sanic_oop/middlewares',
          'sanic_oop/tasks',
      ],
      keywords='sanic oop web api',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Operating System :: POSIX',
      ],
      test_suite="tests", )
