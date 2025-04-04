from setuptools import setup, find_packages

# Ensure UTF-8 encoding
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="pyalert-gmail",
    version="0.1.1",
    author="MisterSoandSo",
    author_email="asoso221@gmail.com",
    description="A Python package for sending email notifications using the Gmail API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MisterSoandSo/pyalert",  
    packages=find_packages(),
    install_requires=[
    "google-api-python-client>=2.165.0",
    "google-auth>=2.38.0",
    "google-auth-httplib2>=0.2.0",
    "google-auth-oauthlib>=1.2.1",
    "requests>=2.32.3",
    "requests-oauthlib>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
