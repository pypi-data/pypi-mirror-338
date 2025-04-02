from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="windsurf-mcp-config-manager",
    version="0.2.1",
    author="Windsurf Team",
    author_email="your.email@example.com",
    description="A utility to manage Windsurf MCP server configurations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trilogy-group/trilogy-group-windsurf-mcp-config-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "click",
        "requests",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "wmcp=windsurf_mcp_config_manager.cli:main",
        ],
    },
)
