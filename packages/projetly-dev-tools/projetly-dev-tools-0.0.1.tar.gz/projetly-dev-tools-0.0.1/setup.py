import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="projetly-dev-tools",
    version="0.0.1",
    author="Roopesh Kumar",
    author_email="roopesh@projetly.ai",
    description=("Projetly dev tool for plugins management."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://projetly@dev.azure.com/projetly/Projetly/_git/Projetly",
    # project_urls={
    #     "Bug Tracker": "https://dev.azure.com/projetly/Projetly/_workitems/recentlyupdated/",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_namespace_packages(include=["projetly_dev_tools*"]),
    package_data={"": ["decorators.py.template", "jwt.py.template", ".env.template", "api_handler.py.template", "auth_handler.py.template", "config.py.template", "events_handler.py.template", "hookresolver.py.template", "request_handler.py.template", "utils.py.template"]},
    include_package_data=True,
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "projetly = projetly_dev_tools.cli:main",
        ]
    }
)   