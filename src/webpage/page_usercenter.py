from .page_home import Home
from django.contrib.auth.models import User
from helpers.authuser.base_data import auth_page_dc
from helpers.director.shortcut import director, ModelFields
from helpers.authuser.models import UserInfo

class UserCenter(Home):
    def __init__(self, request, **kwargs): 
        self.request = request
        self.kw = kwargs
        user =  request.user
        if user.is_authenticated():
            if not hasattr(user, 'userinfo'):
                UserInfo.objects.create(user = user)
        self.field_obj =  UserCentForm(instance = user.userinfo, crt_user= self.request.user, nolimit= True)
        
    def get_template(self, prefer): 
        return 'webpage/usercenter.html'

    def get_heads(self):  
        return self.field_obj.get_heads()

    
    def dict_row(self): 
        user = self.request.user
        if user.is_authenticated():
            if not hasattr(user, 'userinfo'):
                UserInfo.objects.create(user = user)
            dc = {
                'email': user.email,
                'phone': user.userinfo.phone,
                'nickname': user.userinfo.nickname,
                'head': user.userinfo.head,
                '_director_name': 'usercenter_form',
            } 
        else:
            dc = {}
        return dc
    
    def get_context(self):
        page_data = {}
        if self.request.user.is_authenticated():
            page_data['username']= self.request.user.username   
            
        ctx = self.base_context()
        ctx.update( {
            'site_base_template' : 'webpage/site_base.html', 
            'page_data':page_data,
            'heads': self.get_heads(),
            'row': self.field_obj.get_row(),
            'crt_page_name':'usercenter',
            #'header_bar_menu':self.get_header_menu(),
            #'page_menu':self.get_page_menu()
        } )
        return ctx


class UserCentForm(ModelFields):
    class Meta:
        model = UserInfo
        exclude = ['user']
    
    #def is_valid(self): 
        #return True
    
    def getExtraHeads(self): 
        return [
            {'name': 'email','label': '邮箱','editor': 'linetext', 'readonly': True,}, 
        ]
    
    def dict_head(self, head): 
        if head['name'] == 'head':
            head['editor'] = 'com-field-picture'
        if head['name'] == 'phone':
            head['readonly'] = True
        return head
    
    def dict_row(self, inst): 
        user = self.crt_user
        dc = {
            'email': user.email,
            'phone': user.userinfo.phone,
            'nickname': user.userinfo.nickname,
            'head': user.userinfo.head,
        } 
        return dc 
    
    #def save_form(self): 
        #super().save_form()
        #if not hasattr(self.crt_user, 'userinfo'):
            #self.crt_user.userinfo = UserInfo(user = self.crt_user)
        #self.crt_user.userinfo.nickname = self.kw.get('nickname')
        #self.crt_user.userinfo.head = self.kw.get('head')
        #self.crt_user.userinfo.save()
  
    

director.update({
    'usercenter_form': UserCentForm,
})
auth_page_dc.update({
    'usercenter': UserCenter,
})