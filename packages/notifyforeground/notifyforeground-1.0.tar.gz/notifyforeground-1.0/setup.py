""" For Packing """
from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

#☺with open("README.md", "r", encoding="utf-8") as readme_data:
    #long_description = readme_data.read()

requires = []
with open(os.path.join(here, "requirements.txt"),'r') as fp:
    requires = str(fp.read()).split('\n')

setup(
    name="notifyforeground",
    version="1.0",
    author="Hiyabo",
    author_email='hiyabo@yahoo.com',
    description="A Python package that simpilfies creating Android notifications in Kivy apps.",
    url="https://github.com/hiyabo69",
    packages=["notifyforeground"],
    install_requires=requires,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "android",
        "notifications",
        "kivy",
        "mobile",
        "post-notifications",
        "pyjnius",
        "android-notifications",
        "kivy-notifications",
        "python-android",
        "mobile-development",
        'push-notifications',
        'mobile-app',
        'kivy-application'
    ],
    project_urls={
        "Documentation": "https://github.com/hiyabo69",
        # "Documentation": "https://github.com/fector101/android-notify/wiki",
        "Source": "https://github.com/hiyabo69",
        "Tracker": "https://github.com/hiyabo69",
        "Funding": "https://github.com/hiyabo69"
    },
    license="MIT"
)
