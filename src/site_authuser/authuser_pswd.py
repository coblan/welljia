from helpers.authuser.admin_pswd import AuthPwsd, FieldsPage
from helpers.authuser.base_data import auth_page_dc
from webpage.page_home import Home

class SiteAuthPswd(FieldsPage):
    template = 'authuser/changepswd.html'
    need_login = True

    def get_context(self): 
        #ctx = super().get_context()
        ctx = {}
        ctx.update(
            Home(request= self.request).base_context()
        )
        name= self.request.user.username
        dc={
            'site_base_template': 'webpage/site_base.html',
            'login_url':'/%s/login' % self.engin.engin_url,
            'username':name,
            'uid':self.request.user.pk
        }   
        
        ctx.update(dc)
        return ctx

auth_page_dc.update({
     'pswd': SiteAuthPswd,
})