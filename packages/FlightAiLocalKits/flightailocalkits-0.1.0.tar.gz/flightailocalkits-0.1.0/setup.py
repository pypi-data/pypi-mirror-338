from setuptools import setup, find_packages

setup(
    name="FlightAiLocalKits",        # 包名（PyPI 唯一）
    version="0.1.0",          # 版本号
    author="Your Name",
    author_email="your@email.com",
    description="A short description",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],      # 依赖项（可选）
)
