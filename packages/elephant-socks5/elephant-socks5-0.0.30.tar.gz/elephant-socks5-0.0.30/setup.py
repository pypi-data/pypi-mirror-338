# setup.py
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
# install_requires = (this_directory / 'requirements.txt').read_text().splitlines()

__version__ = None

exec(open("elephant_socks5/version.py").read())

config = {
    'name': 'elephant-socks5',
    'url': 'https://github.com/ruanhao/elephant-socks5-client-py',
    'license': 'MIT',
    "long_description": long_description,
    "long_description_content_type": 'text/markdown',
    'description': 'Elephant socks5 tunnel client',
    'author' : 'Hao Ruan',
    'author_email': 'ruanhao1116@gmail.com',
    'keywords': ['proxy', 'http', 'non-blocking', 'py-netty', 'socks5'],
    'version': __version__,
    'packages': find_packages(),
    'install_requires': ['simple-proxy>=0.0.19', 'websocket-client'],
    'python_requires': ">=3.7, <4",
    'setup_requires': ['wheel'],
    'package_data': {'elephant_socks5': ['*']},
    'entry_points': {
        'console_scripts': [
            'elephant = elephant_socks5.__init__:_run',
        ],
    },
    'classifiers': [
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ],
}

setup(**config)
