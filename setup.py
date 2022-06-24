import codecs
import os
import re

from setuptools import setup, find_packages


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)

    return codecs.open(path, mode, encoding)


with open_local(["sanic_template", "__version__.py"], encoding="latin1") as fp:
    try:
        version = re.findall(
            r"^VERSION = \"([^']+)\"\r?$", fp.read(), re.M
        )[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")


setup(
    name='sanic_template',
    version=version,
    description='A template for projects based on Sanic',
    author='prryplatypus',
    author_email='github@prryplatypus.dev',
    packages=find_packages(),
    install_requires=[
        'cerberus',  # Validation
        'databases',  # Database
        'sanic',
        'sanic-ext',
    ],
    extras_require={
        'dev': [
            'black',
            'flake8',
            'isort',
        ]
    }
)
