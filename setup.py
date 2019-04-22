# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['oo', 'oo.sqlalchemy']

package_data = \
{'': ['*'], 'oo.sqlalchemy': ['test/*']}

install_requires = \
['sqlalchemy>=1.3,<2.0']

setup_kwargs = {
    'name': 'oo.sqlalchemy',
    'version': '0.1.0',
    'description': 'SQLAlchemy helpers',
    'long_description': '# oo.sqlalchemy\nSQLAlchemy helpers !',
    'author': 'Jamal Gourinda',
    'author_email': 'jamal.gourinda.pro@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
