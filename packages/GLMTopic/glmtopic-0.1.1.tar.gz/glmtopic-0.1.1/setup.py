from setuptools import setup, find_packages
import os

# Read long description from README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Package data files
package_data_files = []
data_dir = os.path.join('GLMTopic', 'data')
for root, dirs, files in os.walk(data_dir):
    for file in files:
        rel_dir = os.path.relpath(root, 'GLMTopic')
        package_data_files.append(os.path.join(rel_dir, file))

setup(
    name="GLMTopic",
    version="0.1.1",
    author="Junjie Chen, Wenqi Liao, Weisi Chen",
    author_email="example@example.com",  # Replace with actual email
    description="Topic modeling with GLM embeddings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/GLMTopic",  # Replace with actual URL
    packages=find_packages(),
    package_data={
        'GLMTopic': package_data_files,
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "torch",
        "scikit-learn",
        "sentence-transformers",
        "pandas",
        "tqdm",
        "umap-learn",
        "hdbscan",
        "zhipuai",
        "numpy",
        "plotly",
        "matplotlib",
        "jieba",
        "wordcloud",
    ],
) 