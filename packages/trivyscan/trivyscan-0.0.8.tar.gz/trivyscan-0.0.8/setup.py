from setuptools import setup, find_packages

setup(
    name="trivyscan",
    version="0.0.8",
    packages=find_packages(),
    package_data={'': ['*.zip', 'trivy']},
    include_package_data=True,
    install_requires=[],
    author="Alax Alves",
    author_email="alaxallves@gmail.com",
    description="A Python package to run Trivy security scans on Docker images, including the Trivy binary.",
    url="https://github.com/alaxalves/trivyscan",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9'
)
