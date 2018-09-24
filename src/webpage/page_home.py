from django.shortcuts import render
from django.views.generic.base import View
from helpers.director.engine import BaseEngine
#from webpage.models import Banners

from helpers.director.model_func.dictfy import to_dict

# Create your views here.
class Home(View):
    def __init__(self, request = None, **kws):
        super().__init__(**kws)
        self.request = request
        
        
    def get(self,request):
        self.request = request
        ctx = self.get_context()
        template = self.get_template()
        return render(request,template,context=ctx)   
    
    def get_context(self): 
        page_data ={}
        baseengine = BaseEngine()
        baseengine.request = self.request
        
        if self.request.user.is_authenticated():
            page_data['username']= self.request.user.username        
        ctx={
            'page_data':page_data,
            'js_config':baseengine.getJsConfig()
        }
        ctx.update(self.base_context())
        ctx.update( self.extraCtx())
        
        return ctx
    
    def base_context(self): 
        ctx = {}
        ctx.update(self.get_top_heads())
        ctx.update(self.get_header_menu())
        return ctx    
    
    def get_header_menu(self):
        
        dc = { 'header_bar_menu': [
            {'label':'首页','link':'/p/home','name':'home'},
            {'label':'工商注册','link':'/p/3d','name':'3d'},
            {'label':'VR展馆','link':'/p/vr','name':'vr'},
            {'label':'全景现场','link':'/p/fullscreen','name':'fullscreen'},            
        ]}
        return dc
    
    
    def get_top_heads(self): 
        user = self.request.user
        if user.is_authenticated():
            top_head = {
                'top_heads': [
                    {'name': 'userinfo', 'editor': 'com-head-dropdown', 
                     'label': '<i class="fa fa-user-circle"></i>', 
                     'options': [
                        {'url': '/accounts/usercenter', 'label': '修改资料',}, 
                        {'url': '/accounts/pswd', 'label': '修改密码',}, 
                        {'url': '/accounts/logout', 'label': '退出',}
                        ],}
                    ],
            }
        else:
            top_head = {
                'top_heads': [
                    {'name': 'userinfo', 'editor': 'com-head-sm-link',  'options': [
                        {'url': '/accounts/login', 'label': '登录',}, 
                        {'url': '/accounts/regist', 'label': '注册',}, 
                            ],}
                    ],
            }
        return top_head
     
    def extraCtx(self):
        #banners = [{'img': x.img, 'target_url': x.link} for x in Banners.objects.filter(belong = 1).order_by('-priority')]
      
        return {
            #'banners': banners,
            #'recomPanels': recomPanels,
            'crt_page_name':'home',
            #'header_bar_menu':self.get_header_menu(),
            #'page_menu':self.get_page_menu()
        }

    def get_template(self):
        return 'webpage/home.html'
    
