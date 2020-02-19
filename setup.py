import setuptools as st

st.setup(
    version = "0.0.1",
    # package name will be kle-cereal
    # but imported via 'kle' namespace
    name = "kle-cereal",
    description = "",
    keywords = "",
    classifiers = [],
    url = "",
    author = "DamSenViet",
    license = "MIT",
    packages = st.find_packages(exclude=["tests"]),
    install_requires = [],
    python_requires = '>=3.3',
)