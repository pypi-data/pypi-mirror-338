from setuptools import setup, find_packages

setup(
    name="trackers",
    version="1.2.0",
    packages=find_packages(),
    description="A unified library for object tracking",
    author="Piotr Skalski",
    author_email="piotr.skalski92@gmail.com",
    url="https://github.com/roboflow/trackers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)