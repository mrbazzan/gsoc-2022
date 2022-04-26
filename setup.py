import os

from setuptools import setup, Command


class CleanCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -vrf ./build ./dist ./*.pyc ./*.egg-info")


def get_recursive_datafiles(directories):
    """Getting data files recursively."""

    paths = []
    for directory in directories:
        for (path, _, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
    return paths


setup(
    name="transpose",
    version="1.0",
    packages=["transpose"],
    scripts=["bin/transpose"],
    package_data={
        "transpose": get_recursive_datafiles(["transpose/plugins"]),
    },
    author="Erik Skultety",
    author_email="skultety.erik@gmail.com",
    description="modular transposition cipher app",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 or later (GLPv2+)"
    ],
    url="http://example.com",
    cmdclass={
        "clean": CleanCommand,
    },
)
