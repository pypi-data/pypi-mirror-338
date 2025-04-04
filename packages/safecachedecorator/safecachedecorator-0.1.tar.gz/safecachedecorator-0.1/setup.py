from setuptools import setup

setup(
    name="safecachedecorator",
    version="0.1",  # Increment for future updates
    py_modules=["safecache"],
    description="Thread-safe Python caching decorator with TTL",
    author="Pappa1945-tech",
    author_email="your_email@example.com",  # Add your email
    url="https://github.com/Pappa1945-tech/SafeCacheDecorator",
    classifiers=[                          # Add classifiers (optional)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",              # Specify Python version
)