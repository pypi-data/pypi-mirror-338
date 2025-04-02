from setuptools import setup, find_packages

setup(
    name="ice-python",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["stun"],
    author="Dipin Niroula",
    author_email="dipinniroula@hotmail.com",
    description="Interactive Connectivity Establishment (ICE) in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ice_connect",
    license="MIT",
    classifiers=[
         "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
