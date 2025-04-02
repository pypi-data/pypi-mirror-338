from setuptools import setup, find_packages

setup(
    name="Practs",
    version="0.1.0",
    author="Akash Sharma",
    author_email="akashsharma8655@gmail.com",
    description="A simple greeting function",
    long_description=open("C:\\Users\\Akash\\PycharmProjects\\run-terr\\readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/space-add-me/update",  # Replace with your repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)