from setuptools import setup

setup(
    name="delayed_deprecation",
    license="MIT",
    packages=["delayed_deprecation"],
    version="0.1.0",
    description="Delayed deprecation warnings",
    author="Antoine Augusti",
    author_email="hi@antoine-augusti.fr",
    url="https://github.com/AntoineAugusti/delayed_deprecation",
    keywords=["deprecation", "deprecated", "cleaning", "refactor", "refactoring"],
    python_requires=">=3.6",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
