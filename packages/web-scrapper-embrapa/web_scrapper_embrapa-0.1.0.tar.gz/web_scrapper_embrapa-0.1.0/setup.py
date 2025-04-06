from setuptools import setup, find_packages

setup(
    name="web_scrapper_embrapa",
    version="0.1.0",
    author="Tiago Ribeiro",
    author_email="tiagoparibeiro@email.com",
    description="Web Scrapper do site embrapa para curso FIAP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tiagoparibeiro/web_scrapper_embrapa",
    packages=find_packages()
)
