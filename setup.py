import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

tests_require = [
    'pytest-cov',
    'pytest',
    ]

setup(name='kotti_calendar',
      version='0.7a3',
      description="Add a calendar to your Kotti site",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
        ],
      author='Daniel Nouri',
      author_email='daniel.nouri@gmail.com',
      url='http://pypi.python.org/pypi/kotti_calendar',
      keywords='calendar fullcalendar kotti cms pylons pyramid',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Babel',
        'Kotti>=0.7',
        'lingua', ] + tests_require,
      message_extractors={
        '.': [
            ('**.py', 'lingua_python', None),
            ('**.pt', 'lingua_xml', None),
        ]},
      entry_points="""
        [fanstatic.libraries]
        kotti_calendar = kotti_calendar.static:lib
        """,
      )
