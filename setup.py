import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from BrianHG_DDR3 import version_str

setuptools.setup(
    name="pythondata-brianhg-ddr3",
    version=version_str,
    author="Brian HG",
    author_email="BrianHG",
    description="""\
Python module containing hdl files for ddr3 master.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrianHGinc/BrianHG-DDR3-Controller",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Unknown",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'BrianHG_DDR3': ['**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/BrianHGinc/BrianHG-DDR3-Controller/issues",
        "Source Code": "https://github.com/BrianHGinc/BrianHG-DDR3-Controller",
    },
)