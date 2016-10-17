from setuptools import setup, find_packages

setup(
    author = 'Lukas Heinrich',
    author_email = 'lukas.heinrich@gmail.com',
    name = 'cap-schemas',
    version = '0.4.3',
    description = 'schemas for analysis preservation',
    include_package_data = True,
    packages = find_packages(),
    install_requires = [
        'jsonref',
        'pyyaml',
        'requests[security]',
        'jsonschema'
    ]
)
