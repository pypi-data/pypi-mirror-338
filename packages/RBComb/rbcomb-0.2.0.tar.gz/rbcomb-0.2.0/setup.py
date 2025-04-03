from setuptools import setup, find_packages

setup(
    name="RBComb",
    use_scm_version=True,
    setup_requires=["setuptools-scm"],
    description="API to talk to the RBComb bridge",
    long_description_content_type="text/markdown",
    author="Pascal Engeler",
    author_email="huberse@phys.ethz.ch",
    url="https://gitlab.phys.ethz.ch/code/experiment/rbcomb-fpgaCode/",
    packages=find_packages(include=["RBComb", "RBComb.*"]),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.18.0",
        "pyserial>=3.5"
    ]
)

