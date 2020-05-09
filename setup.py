import setuptools as st

st.setup(
    version = "0.0.1",
    # package name will be kle-cereal
    # but imported via 'kle' namespace
    name = "kle-cereal",
    description = "A deserializer for KLE formatted json files.",
    keywords = "keyboard layout editor serial",
    url = "https://github.com/DamSenViet/kle-cereal-python",
    download_url = "https://github.com/DamSenViet/kle-serial-python/tarball/0.0.1",
    author = "DamSenViet",
    license = "MIT",
    namespace_packages=['kle'],
    packages = st.find_packages(exclude=["tests"]),
    install_requires = [],
    python_requires = '>=3.3',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)