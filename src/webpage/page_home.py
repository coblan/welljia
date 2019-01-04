from django.shortcuts import render
from django.views.generic.base import View
from helpers.director.engine import BaseEngine
#from webpage.models import Banners

from helpers.director.model_func.dictfy import to_dict
from helpers.director.kv import get_value
from .models import MapPoint,MainPageItem

# Create your views here.
class Home(View):
    def __init__(self, request = None, **kws):
        super().__init__(**kws)
        self.request = request
        
    def get(self,request):
        self.request = request
        self.projg_pk = request.GET.get('projg')
        self.builds_pk = request.GET.get('builds')
        
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
        if self.request.GET.get('projg'):
            projg = MainPageItem.objects.get(pk=self.projg_pk)
            search_args = {
                'projg':self.projg_pk,
                'builds':self.builds_pk
            }
            builds_menu = []
            for proj in projg.project.all():
                title = proj.title
                pk=proj.pk
                if proj.direct_url:
                    link=proj.direct_url
                elif proj.url:
                    link='/digital?projg=%(projg)s&builds=%(builds)s'%{'projg':projg.pk,'builds':proj.pk}
                else:
                    link=''
                if link:
                    builds_menu.append({
                        'pk':pk,
                        'label':title,
                        'link':link
                    })
            
            dc = { 
                'header_bar_menu': [
                    {'label':'首页','link':'/','name':'full_home'},
                    {'label':'数字沙盘','link':'/digital?projg=%(projg)s&builds=%(builds)s'%search_args,'name':'digital'},
                    {'label':'户型鉴赏','link':'/huxing?projg=%(projg)s&builds=%(builds)s'%search_args,'name':'huxing'},
                    {'label':'区域展示','link':'/zhanshi?projg=%(projg)s&builds=%(builds)s'%search_args,'name':'zhanshi'},
                    #{'label':'商业配套','link':'/peitao','name':'peitao'},
                    {'label':'品牌宣传','link':'/xuanchuan?projg=%(projg)s&builds=%(builds)s'%search_args,'name':'xuanchuan'},   
                    {'label':'项目手册','link':'/manual?projg=%(projg)s&builds=%(builds)s'%search_args,'name':'manual'},  
                ],
                'builds_menu':builds_menu
                #'builds_menu':[
                    #{'pk':x.pk,'label':x.title,'link':'/digital?projg=%(projg)s&builds=%(builds)s'%{'projg':projg.pk,'builds':x.pk}} for x in projg.project.all() if x.url
                #]
            }
        
            return dc
        else:
            return {}
    
    
    def get_top_heads(self): 
        user = self.request.user
        if user.is_authenticated():            
            top_head = {
                'top_heads': [
                    {'name': 'userinfo', 
                     'editor': 'com-head-dropdown', 
                     'mb_editor': 'com-head-sm-link',
                     'label': '<img src="%s" style="display:inline-block;width:24px;height:24px;border-radius:12px;"/>' % (user.userinfo.head or '/static/lib/images/user.png'), #'<i class="fa fa-user-circle"></i>', 
                     'options': [
                        {'link': '/accounts/usercenter', 'label': '个人信息',}, 
                        {'link': '/accounts/pswd', 'label': '修改密码',}, 
                        {'link': '/accounts/logout', 'label': '退出',}
                        ],}
                    ],
            }
        else:
            top_head = {
                'top_heads': [
                    {'name': 'userinfo', 'editor': 'com-head-sm-link',  'options': [
                        {'link': '/accounts/login', 'label': '登录',}, 
                        {'link': '/accounts/regist', 'label': '注册',}, 
                            ],}
                    ],
            }
        return top_head
     
    def extraCtx(self):
        #banners = [{'img': x.img, 'target_url': x.link} for x in Banners.objects.filter(belong = 1).order_by('-priority')]
        
        builds_pk = self.request.GET.get('builds')
        builds = MapPoint.objects.get(pk=builds_pk)
        sha_pan_link =builds.url  #get_value('sha_pan_link')
        return {
            #'banners': banners,
            #'recomPanels': recomPanels,
            'crt_page_name':'digital',
            'link_3d': sha_pan_link
        }

    def get_template(self):
        return 'webpage/home.html'
    


