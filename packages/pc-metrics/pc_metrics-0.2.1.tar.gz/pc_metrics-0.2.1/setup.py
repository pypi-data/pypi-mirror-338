from setuptools import setup, find_packages

setup(
    name="pc_metrics",
    version="0.2.1",
    author="Shu Pu",
    author_email="pushuabc@gmail.com", 
    description="Point Cloud Evaluation Metrics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/URRealHero/point_cloud_metrics",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "numpy>=1.20",
        "scipy>=1.7",
        "scikit-learn>=1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)