try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fitting_tool',
    'author': 'Sudhir Sahu',
    'url': 'https://github.com/sudhir922/fitting_tool',
    'download_url': 'https://github.com/sudhir922/fitting_tool.git',
    'author_email': 'sudhir922@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['fitting_tool'],
    'scripts': [],
    'name': 'fitting_tool'
}

setup(**config)
