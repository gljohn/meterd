try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Meterd',
    'author': 'Gareth John',
    'url': 'https://github.com/gljohn/meterd',
    'download_url': 'https://github.com/gljohn/meterd/archive/master.zip',
    'author_email': 'gljohn@fedoraproject.org',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['meterd'],
    'scripts': [],
    'name': 'meterd'
}

setup(**config)
