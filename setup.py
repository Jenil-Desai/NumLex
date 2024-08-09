import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "NumLex",
    version = "1.0",
    author = "Jenil Desai",
    author_email = "jenildev91@gmail.com",
    description = "A blend of 'Numerical' and 'Lexical' indicating the dual focus on numbers and language.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    project_urls = {
        "Bug Tracker": "https://github.com/Jenil-Desai/NumLex/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)