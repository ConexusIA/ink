from setuptools import setup

setup(
    name="ink-ascii",  # Nombre único en PyPI
    version="0.1.1",  # Incrementa la versión
    py_modules=["generator"],
    install_requires=[
        "pyfiglet",
    ],
    entry_points={
        "console_scripts": [
            "ink=generator:main",
        ],
    },
    author="Tu Nombre",
    author_email="tu@email.com",
    description="A simple tool to generate ASCII art from text.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="URL de tu proyecto (GitHub, GitLab, etc.)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)