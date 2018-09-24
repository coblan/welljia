from helpers.director.engine import BaseEngine,page,fa,can_list,can_touch
from helpers.authuser. base_data import auth_page_dc


class AuthEngine(BaseEngine):
    url_name = 'authengine'
    need_login = False
    


AuthEngine.add_pages(auth_page_dc)