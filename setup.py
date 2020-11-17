import setuptools as st

st.setup(
    version="0.0.0",
    name="damsenviet.kle",
    description="A deserializer for KLE formatted json files.",
    keywords="keyboard layout editor serial",
    url="https://github.com/DamSenViet/kle-cereal-python",
    download_url="https://github.com/DamSenViet/kle-serial-python/tarball/0.0.0",
    author="DamSenViet",
    license="MIT",
    namespace_packages=['damsenviet'],
    packages=st.find_packages(exclude=["tests"]),
    install_requires=[],
    extras_require={
        "test": ["matplotlib>=3.1.2"]
    },
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
