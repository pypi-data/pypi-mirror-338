import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="github-release-update-checker", # Replace with your own username
    version="1.0.1",
    author="1325OK",
    author_email="1325ok.help@gmail.com",
    description="A simple GUI-based update notifier in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1325ok/Python-Github-Release-Update-Checker",
    install_requires=['requests',],
    packages=setuptools.find_packages(),
    package_dir={"": "src"},
    keywords=['github', 'release', 'update', 'checker', 'tkinter','gui'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
