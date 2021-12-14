from setuptools import setup, find_packages

setup(
    author = 'Lukas Heinrich',
    author_email = 'lukas.heinrich@gmail.com',
    name = 'yadage-schemas',
    version = '0.10.6',
    description = 'schemas for yadage and packtivity',
    include_package_data = True,
    packages = find_packages(),
    install_requires = [
        'jsonref',
        'pyyaml',
        'requests[security]>=2.9',
        'jsonschema',
        'click',
        'six>=1.4.0',  # six.moves added in six v1.4.0
    ],
      extras_require = {
        'develop': [
           'pyflakes',
           'pytest>=3.2.0',
           'pytest-cov>=2.5.1',
           'python-coveralls'
        ]
      },
      entry_points = {
      'console_scripts': [
          'yadage-validate=yadageschemas.validatecli:main',
      ],
    }
)
