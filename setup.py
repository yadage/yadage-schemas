from setuptools import setup, find_packages

with open("README.md") as read_file:
    long_description = read_file.read()

setup(
    author = 'Lukas Heinrich',
    author_email = 'lukas.heinrich@gmail.com',
    name = 'yadage-schemas',
    version = '0.10.8',
    description = 'schemas for yadage and packtivity',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    include_package_data = True,
    packages = find_packages(),
    python_requires=">=3.7",
    install_requires = [
        'jsonref',
        'pyyaml',
        'requests[security]>=2.9',
        'jsonschema<=4.9.1',  # c.f. https://github.com/yadage/yadage-schemas/issues/38
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
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Operating System :: OS Independent",
    ]
)
