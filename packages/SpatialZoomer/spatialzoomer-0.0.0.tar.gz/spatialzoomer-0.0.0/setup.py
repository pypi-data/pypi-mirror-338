from setuptools import setup, find_packages
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='SpatialZoomer',
    version='0.0.0',
    description="SpatialZoomer",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    include_package_data=True,
    author='Xinqi Li',
    author_email='lxq19@mails.tsinghua.edu.cn',
    license='MIT License',
    url='https://github.com/Li-Xinqi/SpatialZoomer.git',
    packages=find_packages(include=['SpatialZoomer', 'SpatialZoomer.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.8',
)