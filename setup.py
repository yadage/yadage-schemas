from setuptools import setup, find_packages

setup(
    author = 'Lukas Heinrich',
    author_email = 'lukas.heinrich@gmail.com',
    name = 'yadage-schemas',
    version = '0.7.4',
    description = 'schemas for yadage and packtivity',
    include_package_data = True,
    packages = find_packages(),
    install_requires = [
        'jsonref',
        'pyyaml',
        'requests[security]>=2.9',
        'jsonschema',
        'click',
    ],
    entry_points = {
      'console_scripts': [
          'yadage-validate=yadageschemas.validatecli:main',
      ],
    }
)
