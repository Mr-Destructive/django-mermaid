import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "0.1.89"
PACKAGE_NAME = "django-mermaid"
AUTHOR = "Meet Gor"
AUTHOR_EMAIL = "gormeet711@gmail.com"
URL = "https://github.com/Mr-Destructive/crossposter"

DESCRIPTION = (
    "Generate Mermaid ER Diagrams for your django projects!"
)

INSTALL_REQUIRES = [
    "django",
    "rich",
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    entry_points={"console_scripts": 
        [
            "djmaid = django_mermaid.app:main",
            "maidj = django_mermaid.app:generate_model",
        ]
    },
)
