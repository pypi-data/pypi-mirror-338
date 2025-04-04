from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp_agent_tools",
    version="0.1.0",
    author="esragoth",
    author_email="beppe.wizzy@gmail.com",
    description="Tools to connect MCP servers with AI agent frameworks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esragoth/mcp_agent_tools",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "aiohttp",
        "websockets",
        "pydantic>=2.0.0",
        "mcp",
    ],
    extras_require={
        "smolagents": ["smolagents"],
        "dev": ["pytest", "black", "isort", "mypy"],
    },
) 