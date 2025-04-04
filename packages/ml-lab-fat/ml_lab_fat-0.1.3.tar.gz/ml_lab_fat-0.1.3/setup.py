from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ml_lab_fat",
    version="0.1.3", 
    packages=find_packages(),
    entry_points={"console_scripts": ["ml_lab_fat=ml_lab_fat.main:show_options"]},
    long_description=long_description,  
    long_description_content_type="text/markdown",  
)
