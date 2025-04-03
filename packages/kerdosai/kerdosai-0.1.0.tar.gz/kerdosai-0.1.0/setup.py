from setuptools import setup, find_packages

setup(
    name="kerdosai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.0.0",
        "tqdm>=4.65.0",
    ],
    author="KerdosAI Team",
    author_email="support@kerdosai.com",
    description="Universal LLM Training Agent",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kerdosai/kerdosai",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
) 