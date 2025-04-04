from setuptools import setup, find_packages

setup(
    name="dttuong",  # Tên thư viện của bạn
    version="0.1",  # Phiên bản đầu tiên
    author="Tuongne0706",
    author_email="zzxr851@gmail.com",
    description="A library for learning and research purposes on image processing, performing piecewise linear transformations on grayscale and color images.",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuong0706/dttuong",  # Đặt link tới repository GitHub của bạn (nếu có)
    packages=find_packages(),
    install_requires=[  # Các thư viện phụ thuộc
        "opencv-python",
        "numpy",
        "matplotlib",
        "scikit-learn"
    ],
    classifiers=[  # Các phân loại thư viện
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
