from setuptools import setup, find_packages

setup(
    name="pasargad",
    version="5.0.0",
    author="ramox",
    author_email="actramox@gmail.com",
    description="An ultra-strong DDoS and attack protection library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pasargadcdn",
    packages=find_packages(),
    package_data={
        "pasargad": ["*.py"],  # شامل همه فایل‌های .py توی پوشه pasargad
    },
    include_package_data=True,
    install_requires=[
        "scapy>=2.4.5",
        "psutil>=5.9.0",
        "numpy>=1.23.0",
        "pandas>=1.5.0",
        "redis>=4.0.0",
        "scikit-learn>=1.0.0",
        "requests>=2.28.0",
        "maxminddb>=2.0.0",  # برای GeoIP
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)