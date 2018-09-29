from django.shortcuts import render
from .page_home import Home
from .models import ZhanRich
from helpers.director.model_func.dictfy import sim_dict
# Create your views here.
class ZhanShi(Home):
    def get_template(self): 
        return 'webpage/zhanshi.html'
    
    def extraCtx(self): 
        pageitems = [sim_dict(x) for x in ZhanRich.objects.filter(page = 'zhanshi').order_by('-priority')]
        return {
            'crt_page_name':'zhanshi',
            'pageitems': pageitems,
        }

class Xuanchuan(Home):
    def get_template(self): 
        return 'webpage/zhanshi.html'
    
    def extraCtx(self): 
        pageitems = [sim_dict(x) for x in ZhanRich.objects.filter(page = 'xuanchuan').order_by('-priority')]
        return {
            'crt_page_name':'xuanchuan',
            'pageitems': pageitems,
        }    