from setuptools import setup, find_packages

setup(
    author = 'Lukas Heinrich',
    author_email = 'lukas.heinrich@gmail.com',
    name = 'yadage-schemas',
    version = '0.10.7',
    description = 'schemas for yadage and packtivity',
    include_package_data = True,
    packages = find_packages(),
    # Support Python 3.7+ but keep legacy support for Python 2.7 until 2022
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*",
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
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Operating System :: OS Independent",
    ]
)
