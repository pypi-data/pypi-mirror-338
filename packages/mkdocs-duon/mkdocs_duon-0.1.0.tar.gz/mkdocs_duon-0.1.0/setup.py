from setuptools import find_packages, setup

VERSION = "0.1.0"

with open("README.md", "rt", encoding="utf8") as f:
    README = f.read()

setup(
    name="mkdocs-duon",
    version=VERSION,
    url="https://github.com/duoncode/mkdocs-theme",
    license="MIT",
    description="Default mkdocs theme for Duon projects",
    long_description=README,
    long_description_content_type="text/markdown",
    author="ebene fünf GmbH",
    author_email="duon@ebenefuenf.de",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mkdocs>=1.6",
        "mkdocs-macros-plugin>=0.7",
        "pymdown-extensions>=10.3",
    ],
    entry_points={
        "mkdocs.themes": [
            "duon = theme",
        ]
    },
    zip_safe=False,
)
