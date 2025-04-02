from setuptools import setup, find_packages

setup(
    name="pasargad",
    version="4.0.0",
    author="ramox",
    author_email="actramox@gmail.com",
    description="An ultra-strong DDoS and attack protection library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pasargadcdn",
    packages=find_packages(),
    install_requires=[
        "scapy>=2.4.5",
        "psutil>=5.9.0",
        "numpy>=1.23.0",  # برای الگوریتم‌های یادگیری ماشین
        "pandas>=1.5.0",  # برای تحلیل داده‌ها
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)