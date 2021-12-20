from setuptools import setup

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name="trackr",
    version="0.0.1",
    author="Pranav Baburaj",
    author_email="i.am.pranav.baburaj@gmail.com",
    py_modules=["main"],
    description="Track app time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=classifiers,
    python_requires=">=3.6",
    install_requires=["psutil", "plyer", "prettytable"],
    entry_points={
        "console_scripts": ["trackr=main:main"],
    },
)