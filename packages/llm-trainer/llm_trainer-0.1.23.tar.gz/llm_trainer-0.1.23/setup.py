import os
from setuptools import setup, find_packages

# Add description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

# Parse requirements from requirements.txt
try:
    with open(os.path.join(current_directory, 'requirements.txt'), encoding='utf-8') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    print("requirements.txt not found, using default requirements.")
    requirements = [
        'torch==2.6.0',
        'numpy==2.2.3',
        'transformers==4.49.0',
        'datasets==3.3.2',
        'tqdm==4.67.1',
        'matplotlib==3.10.1'
    ]
except IOError as e:
    print(f"IOError occurred while reading requirements.txt: {e}")
    requirements = []

setup(
    name='llm_trainer',
    packages=find_packages('.'),
    version='0.1.23',
    license='MIT',
    description='🤖 Train your LLMs with ease and fun .',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Nikoláy Skripkó',
    author_email='nskripko@icloud.com',
    url='https://github.com/Skripkon/llm_trainer',
    keywords=[],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.11',
)
