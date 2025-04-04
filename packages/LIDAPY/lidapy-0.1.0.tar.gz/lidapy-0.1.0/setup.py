from setuptools import setup, find_packages

setup(
    name="LIDAPY",
    version="0.1.0",
    packages=find_packages(include=["source*"]),  # Explicitly include only your package
    exclude_package_data={"": ["Tests", "Configs"]},  # Exclude directories
    install_requires=[
        "requests",
    ],
    author="Brian W Karimi, Katie Killian, Nicole Vadillo",
    description="A Python framework for the LIDA Framework"
)