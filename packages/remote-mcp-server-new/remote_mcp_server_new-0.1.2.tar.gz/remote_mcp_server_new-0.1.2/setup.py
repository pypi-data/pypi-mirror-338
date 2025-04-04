from setuptools import setup

setup(
    name="remote_mcp_server_new",
    version="0.1.2",
    description="Remote MCP Server",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.13",
    install_requires=[
        "fastapi[standard]>=0.115.12",
        "httpx>=0.28.1",
        "mcp[cli]>=1.6.0",
        "pydantic>=2.11.1",
        "requests>=2.32.3",
        "setuptools>=78.1.0",
        "uvicorn[standard]>=0.34.0",
    ],
    package_dir={"": "src"},
    py_modules=["server"],  # if src/server.py is the main module
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
