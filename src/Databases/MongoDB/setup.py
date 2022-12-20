from __future__ import annotations

from pathlib import Path

import setuptools


def read_multiline_as_list(file_path: str) -> list[str]:
    with open(file_path) as fh:
        contents = fh.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


def get_optional_requirements() -> dict[str, list[str]]:
    """Get dict of suffix -> list of requirements."""
    requirements_files = Path(".").glob(r"requirements-*.txt")
    requirements = {
        p.stem.split("-")[-1]: read_multiline_as_list(p) for p in requirements_files
    }
    return requirements


requirements = read_multiline_as_list("requirements.txt")
opt_requirements = get_optional_requirements()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mongodb",
    version="1.0.0",
    author="Teialabs",
    author_email="contato@teialabs.com",
    description="Teia Project-Template databases package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeiaLabs/AthenaAPI/",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require=opt_requirements,
)
