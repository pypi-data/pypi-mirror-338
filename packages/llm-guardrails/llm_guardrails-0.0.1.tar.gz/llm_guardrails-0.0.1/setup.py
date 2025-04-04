from setuptools import setup, find_packages

setup(
    name="llm-guardrails",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="research@lasso.security",
    description="A package for LLM guardrails",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lasso-security/llm-guardrails",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
