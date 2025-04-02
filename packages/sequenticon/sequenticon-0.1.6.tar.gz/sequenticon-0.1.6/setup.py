from setuptools import setup, find_packages

version = {}
with open("sequenticon/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="sequenticon",
    version=version["__version__"],
    author="Zulko",
    description="Generate human-friendly icons from DNA sequences",
    long_description=open("pypi-readme.rst").read(),
    license="MIT",
    keywords="DNA sequence barcoding sequenticon identicon hash",
    packages=find_packages(exclude="docs"),
    include_package_data=True,
    install_requires=[
        "Biopython",
        "pydenticon",
        "snapgene_reader",
        "flametree",
        "pdf_reports",
    ],
)
