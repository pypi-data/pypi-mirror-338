from setuptools import setup, find_packages

setup(
    name="ethcoinerdater",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],  # Dependencies
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple tool to get ETH prices from CoinGecko",
    license="MIT",
    url="https://github.com/yourusername/ethcoinerdater",
)
