from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='practice_hello',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
        #ex 'numpy>=1.11.1'
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)