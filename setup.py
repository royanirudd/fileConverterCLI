from setuptools import setup, find_packages

setup(
    name="file_converter",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow",  # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'converter = converter:main',  # Points to the main function in converter.py
        ],
    },
    description="A command-line tool for converting files between compatible formats.",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/your_username/file_converter",  # Replace with your GitHub URL
)

