from .client import QiitaClient
from .classes import QiitaArticle, QiitaUser

class QiitaClient2(QiitaClient):
    """ Qiita API Client with structured response objects."""
    
    def get_item(self, item_id):
        """ Fetch a specific Qiita article and return as QiitaArticle object."""
        item = super().get_item(item_id)
        return QiitaArticle(item.to_json())

    def get_user(self, user_id):
        """ Fetch a specific Qiita user and return as QiitaUser object."""
        user = super().get_user(user_id)
        return QiitaUser(user.to_json())
    
    def list_user_items(self, user_id, params=None, headers=None):
        """ Fetch a list of articles by a specific user and return as a list of QiitaArticle objects."""
        items = super().list_user_items(user_id, params, headers)
        return [QiitaArticle(item) for item in items.to_json()]
    
    def list_items(self, params=None, headers=None):
        """ Fetch all articles in descending order and return as a list of QiitaArticle objects."""
        items = super().list_items(params, headers)
        return [QiitaArticle(item) for item in items.to_json()]
    
    def list_tag_items(self, tag_id, params=None, headers=None):
        """ Fetch a list of articles with a specific tag and return as a list of QiitaArticle objects."""
        items = super().list_tag_items(tag_id, params, headers)
        return [QiitaArticle(item) for item in items.to_json()]
    
    def list_user_stocks(self, user_id, params=None, headers=None):
        """ Fetch a list of stocked articles by a user and return as a list of QiitaArticle objects."""
        items = super().list_user_stocks(user_id, params, headers)
        return [QiitaArticle(item) for item in items.to_json()]
    
    def get_authenticated_user_items(self, params=None, headers=None):
        """ Fetch authenticated user's articles and return as a list of QiitaArticle objects."""
        items = super().get_authenticated_user_items(params, headers)
        return [QiitaArticle(item) for item in items.to_json()]
    
    def list_users(self, params=None, headers=None):
        """ Fetch all users and return as a list of QiitaUser objects."""
        users = super().list_users(params, headers)
        return [QiitaUser(user) for user in users.to_json()]
    
    def get_authenticated_user(self, params=None, headers=None):
        """ Fetch the authenticated user's information and return as a QiitaUser object."""
        user = super().get_authenticated_user(params, headers)
        return QiitaUser(user.to_json())
    
    def list_user_followees(self, user_id, params=None, headers=None):
        """ Fetch a list of users followed by a specific user and return as a list of QiitaUser objects."""
        users = super().list_user_followees(user_id, params, headers)
        return [QiitaUser(user) for user in users.to_json()]
    
    def list_user_followers(self, user_id, params=None, headers=None):
        """ Fetch a list of users following a specific user and return as a list of QiitaUser objects."""
        users = super().list_user_followers(user_id, params, headers)
        return [QiitaUser(user) for user in users.to_json()]
    
    def list_item_stockers(self, item_id, params=None, headers=None):
        """ Fetch a list of users who stocked a specific item and return as a list of QiitaUser objects."""
        users = super().list_item_stockers(item_id, params, headers)
        return [QiitaUser(user) for user in users.to_json()]
