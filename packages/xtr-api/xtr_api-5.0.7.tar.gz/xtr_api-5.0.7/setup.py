from setuptools import setup, find_packages
try:
    from xtr_api.static._info import __name__, __version__
except Exception as e:
    __name__ = 'xtr_api'
    __version__ = '5.0.7'


setup(
    name=__name__,
    version=__version__,
    packages=find_packages(),
    description=__name__,
    long_description_content_type='text/plain',
    long_description="""This Python library simplifies the creation of extraction APIs to streamline file parsing for data science workflows. It provides intuitive abstractions for reading and transforming data from diverse file formats—like CSV, JSON, and more—letting you focus on insights rather than low-level parsing details. By centralizing and standardizing your data ingestion process, it accelerates development and ensures consistent, reliable results for any data science project.""",
    url='https://github.com/choll/xtr',
    download_url='https://github.com/choll/xtr',
    project_urls={
        'Documentation': 'https://github.com/choll/xtr'},
    author='Tom Christian',
    author_email='tom.christian@openxta.com',
)
