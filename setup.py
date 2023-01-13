import setuptools


with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="statistics_dispersion",
    version="0.0.1",
    author="Mahdi-Zarepour",
    author_email="mahdizarepour40@gmail.com",
    packages=["statistics_dispersion"],
    description="dispersion in Python",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahdi-zarepour/dispersion",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
