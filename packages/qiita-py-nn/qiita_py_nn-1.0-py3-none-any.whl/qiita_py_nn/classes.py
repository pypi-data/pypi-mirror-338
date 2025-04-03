class QiitaArticle:
    def __init__(self, dict_data):
        self.body = dict_data["body"]
        self.coediting = dict_data["coediting"]
        self.comments_count = dict_data["comments_count"]
        self.created_at = dict_data["created_at"]
        self.group = dict_data["group"]
        self.id = dict_data["id"]
        self.likes_count = dict_data["likes_count"]
        self.organization_url_name = dict_data["organization_url_name"]
        self.page_views_count = dict_data["page_views_count"]
        self.private = dict_data["private"]
        self.reactions_count = dict_data["reactions_count"]
        self.rendered_body = dict_data["rendered_body"]
        self.slide = dict_data["slide"]
        self.stocks_count = dict_data["stocks_count"]
        self.tags = dict_data["tags"]
        self.team_membership = dict_data["team_membership"]
        self.title = dict_data["title"]
        self.updated_at = dict_data["updated_at"]
        self.url = dict_data["url"]
        self.user = dict_data["user"]
    
    def __repr__(self):
        return (
            f"QiitaArticle("
            f"body={(self.body[0:50])!r}, coediting={self.coediting!r}, comments_count={self.comments_count!r}, "
            f"created_at={self.created_at!r}, group={self.group!r}, id={self.id!r}, "
            f"likes_count={self.likes_count!r}, organization_url_name={self.organization_url_name!r}, "
            f"page_views_count={self.page_views_count!r}, private={self.private!r}, "
            f"reactions_count={self.reactions_count!r}, rendered_body={self.rendered_body[0:50]}, "
            f"slide={self.slide!r}, stocks_count={self.stocks_count!r}, tags={self.tags!r}, "
            f"team_membership={self.team_membership!r}, title={self.title!r}, updated_at={self.updated_at!r}, "
            f"url={self.url!r}, user={self.user!r})"
        )

class QiitaUser:
    def __init__(self, dict_data):
        self.description = dict_data["description"]
        self.facebook_id = dict_data["facebook_id"]
        self.followees_count = dict_data["followees_count"]
        self.followers_count = dict_data["followers_count"]
        self.github_login_name = dict_data["github_login_name"]
        self.id = dict_data["id"]
        self.items_count = dict_data["items_count"]
        self.linkedin_id = dict_data["linkedin_id"]
        self.location = dict_data["location"]
        self.name = dict_data["name"]
        self.organization = dict_data["organization"]
        self.permanent_id = dict_data["permanent_id"]
        self.profile_image_url = dict_data["profile_image_url"]
        self.team_only = dict_data["team_only"]
        self.twitter_screen_name = dict_data["twitter_screen_name"]
        self.website_url = dict_data["website_url"]
    
    def __repr__(self):
        return (
            f"QiitaUser("
            f"description={self.description!r}, facebook_id={self.facebook_id!r}, "
            f"followees_count={self.followees_count!r}, followers_count={self.followers_count!r}, "
            f"github_login_name={self.github_login_name!r}, id={self.id!r}, items_count={self.items_count!r}, "
            f"linkedin_id={self.linkedin_id!r}, location={self.location!r}, name={self.name!r}, "
            f"organization={self.organization!r}, permanent_id={self.permanent_id!r}, "
            f"profile_image_url={self.profile_image_url!r}, team_only={self.team_only!r}, "
            f"twitter_screen_name={self.twitter_screen_name!r}, website_url={self.website_url!r})"
        )