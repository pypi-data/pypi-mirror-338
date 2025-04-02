from setuptools import setup              
            

setup(
    name="pickshot", 
    version='0.1.0',
    author="Jakub Kubis - JBS",
    author_email="jbiosystem@gmail.com",
    description='PickShot - Python package for CNN-based filtering of low-quality images from analysis',
    long_description="""
        PickShot - Python Package for Automated Image Quality Assessment with CNNs
        PickShot is a powerful Python package designed to facilitate the training and deployment of Convolutional Neural Network (CNN) models for automatic quality assessment of microscopy or imaging cytometry data.

        This tool allows users to:

        * Train custom models on user-selected high-quality and low-quality images.
        * Automatically classify and filter images based on quality, streamlining the process of collecting, processing, and analyzing large datasets.
        """,    
    url="https://github.com/jkubis96/PickShot/tree/main",    
    packages=['pickshot'],
    include_package_data=True,
    install_requires= [
        "numpy (>=1.26.0,<2.2.0)",
        "tensorflow (>=2.19.0,<3.0.0)",
        "opencv-python (>=4.11.0.86,<5.0.0.0)",
        "tqdm (>=4.67.1,<5.0.0)",
        "scikit-learn (>=1.6.1,<2.0.0)",
        "joblib (>=1.4.2,<2.0.0)",
        "requests (>=2.32.3,<3.0.0)",
        "tifffile (>=2025.3.30,<2026.0.0)",
    ],       
    keywords=['CNN', 'ML', 'QC', 'Flow cytometry', 'images', 'drop', 'microscopy'],
    license='GPL-3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.12,<3.13"
   
)
