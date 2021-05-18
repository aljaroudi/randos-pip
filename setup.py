from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='randos',
    packages=find_packages(where="src"),
    version='0.0.4',
    description='A randomness library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    author='Mohammed Aljaroudi',
    author_email='maljaroudi@sandiego.edu',
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[],
    tests_require=['pytest>=3', ],
    url='https://github.com/aljaroudi/randos-pip'
)
