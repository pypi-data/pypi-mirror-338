from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import os
import sys

# Configuración básica para todas las plataformas
extra_compile_args = ['-O3']
extra_link_args = []

extensions = [
    Extension(
        "kagent_cli.client",
        ["src/kagent_cli/client.py"],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    ),
    Extension(
        "kagent_cli.__main__",
        ["src/kagent_cli/__main__.py"],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args
    )
]

setup(
    name="kagent-cli",
    version="0.1.5",
    description="KaioAgent Client (Compiled)",
    author="Silicon UY",
    author_email="dev@siliconuy.com",
    url="https://github.com/siliconuy/kagent-dev",
    long_description="A simple and efficient client for KaioAgent services.",
    long_description_content_type="text/plain",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            'language_level': "3",
            'boundscheck': False,
            'wraparound': False
        }
    ),
    python_requires=">=3.7",
    install_requires=[
        "asyncio>=3.4.3",
        "websockets>=9.1",
        "aiohttp>=3.7.4"
    ],
    entry_points={
        "console_scripts": [
            "kagent-cli=kagent_cli.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
