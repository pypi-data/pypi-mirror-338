from setuptools import setup, find_packages

setup(
    name="sandbox-browser",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "docker>=6.1.3",
        "python-dotenv>=1.0.0",
    ],
    author="Zhang Yi",
    author_email="yi.zhang1@brgroup.com",
    description="A sandbox environment for browser automation with VNC support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sandbox-browser",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
) 