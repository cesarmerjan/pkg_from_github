import pathlib

from setuptools import setup

BASEDIR = pathlib.Path(__file__).parent
README = (BASEDIR / "README.md").read_text()

setup(
    name="Test Package",
    python_requires=">3.9",
    version="0.1.2",
    description="Used to sign strings.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cesarmerjan/pkg_from_github",
    download_url="https://github.com/cesarmerjan/pkg_from_github/archive/refs/heads/master.zip",
    author="Cesar Merjan",
    author_email="cesarmerjan@gmail.com",
    keywords=["test"],
    license="MIT",
    include_package_data=True,
    package_dir={"": "src"},
    packages=["pkg_from_github"],
    classifiers=[],
    install_requires=["pandas"],
)
