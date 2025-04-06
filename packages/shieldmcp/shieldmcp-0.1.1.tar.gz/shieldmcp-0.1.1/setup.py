from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# ASCII Art for the package
ASCII_ART = r"""     _     _      _     _                      
 ___| |__ (_) ___| | __| |_ __ ___   ___ _ __  
/ __| '_ \| |/ _ \ |/ _` | '_ ` _ \ / __| '_ \ 
\__ \ | | | |  __/ | (_| | | | | | | (__| |_) |
|___/_| |_|_|\___|_|\__,_|_| |_| |_|\___| .__/ 
                                        |_|    
"""

setup(
    name="shieldmcp",
    version="0.1.1",
    author="x3at",
    author_email="xiomaraengine@gmail.com",
    description=ASCII_ART + "\nA security middleware for Model Context Protocol (MCP) servers that enhances security and monitoring capabilities without modifying the official SDK. This package provides tools for securing and monitoring MCP tool calls, following the best practices outlined in the MCP documentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shieldmcp/shieldmcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=[
        "structlog>=21.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.12",
            "black>=21.5b2",
            "isort>=5.9.3",
            "mypy>=0.910",
            "flake8>=3.9.2",
        ],
    },
) 