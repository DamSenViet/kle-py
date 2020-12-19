from os import path
import setuptools as st

long_description: str
with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as file:
    long_description = file.read()

st.setup(
    version="0.0.0",
    name="damsenviet.kle",
    description="A Python library for interacting with KLE data structures and files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DamSenViet/kle-py",
    download_url="https://github.com/DamSenViet/kle-py/tarball/0.0.0",
    project_urls={
        "Source": "https://github.com/DamSenViet/kle-py",
        "Documentation": "https://damsenviet.github.io/kle-py/",
    },
    author="DamSenViet",
    license="MIT",
    namespace_packages=["damsenviet"],
    packages=st.find_packages(),
    install_requires=[
        "typeguard>=2.10.0",
        "tinycss2>=1.1.0",
    ],
    extras_require={
        "dev": [
            # test dependencies
            "matplotlib>=3.1.2",
            "pytest>=6.1.2",
            # formatting
            "black>=20.8b1",
            # docs
            "sphinx>=3.3.1",
            "pydata-sphinx-theme>=0.4.1",
        ],
    },
    python_requires=">=3.7",
    keywords="keyboard layout editor serial",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
