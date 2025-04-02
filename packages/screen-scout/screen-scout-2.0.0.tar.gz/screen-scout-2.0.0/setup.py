from setuptools import setup, find_packages

setup(
    name="screen-scout",
    version="2.0.0",
    description="Automated UI testing tool",
    author="ScreenScout Team",
    author_email="team@usescreenscout.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "nest_asyncio"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "screen-scout = main:main"
        ]
    },
)
