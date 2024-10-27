from setuptools import setup, find_packages

setup(
    name="file_converter",
    version="1.0",
    packages=find_packages(),  # This will include your package and any subpackages
    install_requires=[
        "Pillow",
    ],
    entry_points={
        'console_scripts': [
            'converter=file_converter:main',  # This should point to your main function in converter.py
        ],
    },
)

