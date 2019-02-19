from setuptools import setup, find_packages


setup(
    name="hugaton",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "boto3",
    ],
    extras_require={
        "dev": [
            "flake8",
            "black",
            "coverage",
            "tox",
            "pytest",
            "pytest-mock",
        ],
    },
    python_requires=">=3.8, <4",
)
