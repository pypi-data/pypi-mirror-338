from setuptools import setup, find_packages

with open('utils/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="tshine73-utils",
    version="0.1.1",
    author="tshine73",
    author_email="fan.steven.chiang@gmail.com",
    description="no description",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    include_package_data=True
)
