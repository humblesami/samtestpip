from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='number_utility',
    version='0.0.3',
    description='Test package.',
    py_modules=["samtestpip"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sami Akram S M",
    author_email="samiakram@live.com",
    url="https://github.com/humblesami/samtestpip"
)