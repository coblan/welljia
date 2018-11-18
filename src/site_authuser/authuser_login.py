from helpers.authuser.admin_login import LoginFormPage, auth_page_dc, director
import re
from django.contrib.auth.models import User
from usersystem.models import UserInfo

class SiteLoginFormPage(LoginFormPage):
    def get_context(self): 
        ctx = super().get_context()
        next_url= self.request.GET.get('next','/')
        dc={
            'page_cfg': {     
                'next':next_url,
                'title': '用户登录',
                'subtitle': '欢迎登录威尔佳',
                'regist_url': '%s/regist' % self.engin.engin_url,
                'copyright': 'Copyright @2018  All Right Reserve',
                'heads': self.get_heads(),
                'login_item': '手机号',
                
                },
        } 
        
        ctx.update(dc)
        return ctx
    
    @staticmethod
    def do_login(username,password,auto_login=False):
        """
        登录函数：
        """
        try:
            if re.search('^\w+@\w+', username):
                real_name = User.objects.get(email = username).username
            elif re.search('^\d{11}', username):
                real_name = UserInfo.objects.get(phone = username).user.username
            else:
                return {'errors': {'username': ['请输入正确的邮箱或者手机号'],},}
            return LoginFormPage.do_login(real_name, password)
        except (User.DoesNotExist , UserInfo.DoesNotExist):
            return {'errors': {'username': ['用户不存在'],},}

director.update({
    'do_login': SiteLoginFormPage.do_login,
})

auth_page_dc .update({
    'login': SiteLoginFormPage,
})