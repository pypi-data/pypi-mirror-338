Python Wrapper for Qiita API v2
===============================

Python wrapper for Qiita API.

Fork from qiita_v2(https://github.com/petitviolet/qiita_py).

Version
-------

1.0(2025/04/01)

Setup
-----

`qiita_v2: Python Package Index <https://pypi.python.org/pypi/qiita_py_nn>`_
::

  pip install qiita_py_nn

How to Use
----------

Simple usage
~~~~~~~~~~~~

::

  from qiita_py_nn.client2 import QiitaClient2

  client = QiitaClient2(access_token=<access_token>)

  user = client.get_user("nekoniii3")

  print(user)
  # QiitaUser(description= ... , website_url='')

Caution
----------

Version1.0 The following methods are supported:

::

  get_item
  get_user
  list_user_items
  list_items
  list_tag_items
  list_user_stocks
  get_authenticated_user_items
  list_users
  get_authenticated_user
  list_user_followees
  list_user_followers
  list_item_stockers

Reference
----------

`Qiita Article <https://qiita.com/nekoniii3/items/1610ec2b03cb9cd38f44/>`_

Lisence
-------

`MIT License <http://petitviolet.mit-license.org/>`_
