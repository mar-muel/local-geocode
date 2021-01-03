import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="local-geocode", # Replace with your own username
    version="0.0.1",
    author="Martin Müller",
    author_email="martin.mathias.mueller@gmail.com",
    description="Simple library for efficient geocoding without making API calls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mar-muel/local-geocode",
    packages=setuptools.find_packages(),
    package_data={'geocode': ['data/*.pkl']},
    install_requires=[
        'pandas',
        'tqdm',
        'flashtext',
        'joblib'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
