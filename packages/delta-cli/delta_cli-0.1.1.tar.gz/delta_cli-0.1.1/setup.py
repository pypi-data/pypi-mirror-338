from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="delta-cli",
    version="0.1.1",
    author="arstech",
    author_email="arstechai@gmail.com",  # Email adresinizi girin
    description="Delta CLI - Ağ yönetimi ve AI asistanı için komut satırı aracı",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/delta-cli",  # GitHub repo URL'nizi girin
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'openai',
        'colorama',
        'rich',
        'tabulate',
        'speedtest-cli',
        'dnspython',
        'requests',
        'psutil',
        'cryptography',
        'wmi'
    ],
    entry_points={
        'console_scripts': [
            'delta=delta.cli:main',
        ],
    },
    python_requires='>=3.8',
    include_package_data=True,
)
