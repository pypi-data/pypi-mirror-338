from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read the version from version.py
with open("clip_streamlit/version.py", encoding="utf-8") as f:
    exec(f.read())

setup(
    name="clip-streamlit",
    version=__version__,
    author="fake-babu",
    author_email="apunfakebabu@gmail.com",
    description="Zero-shot image classification using CLIP and Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fake-babu/clip-streamlit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "streamlit>=1.0.0",
        "torch>=1.7.0",
        "Pillow>=8.0.0",
    ],
    package_data={
        'clip_streamlit': ['install_deps.sh'],
    },
    entry_points={
        "console_scripts": [
            "clip-streamlit=clip_streamlit.app:run_app",
        ],
    },
)