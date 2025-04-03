from setuptools import setup, find_packages 
 
with open("README.md", "r", encoding="utf-8") as fh: 
 
    long_description = fh.read() 
 
setup( 
 
    name="neuropipeline2",  # Replace with your package name 
 
    version="0.1.0",  # Initial version number 
 
    author="Adam Emile Aske", 
 
    author_email="adamaske@outlook.com", 
 
    description="A short description of your package", 
 
    long_description=long_description, 
 
    long_description_content_type="text/markdown", 

    license_file="LICENSE",
 
    url="https://github.com/adamaske/neuropipeline2",  # Replace with your repository URL 
 
    packages=find_packages(), 
 
    classifiers=[ 
 
        "Programming Language :: Python :: 3", 
 
        "License :: OSI Approved :: MIT License",  # Replace with your license 
 
        "Operating System :: OS Independent", 
 
    ], 
 
    python_requires='>=3.6', # minimum python version required
 
    install_requires=[ 
 
        # List your package's dependencies here 
 
        # "requests>=2.25.0", 
        "numpy",
        "pandas",
        "mne",
        "mne-nirs",
        "matplotlib",
        "snirf",
        "nilearn",
        "pylsl",
        "scipy",
        "h5py",
        "pywavelets",
        "pyedflib",
    ], 
 
) 
