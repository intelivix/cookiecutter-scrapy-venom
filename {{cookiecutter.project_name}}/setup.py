# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.project_name}}',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = {{cookiecutter.project_name}}.settings']},
)
