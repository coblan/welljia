from django.shortcuts import render
from .page_home import Home
from .models import ZhanRich, MapPoint, Area, MainPageItem, PageImages
from helpers.director.model_func.dictfy import sim_dict
# Create your views here.



class FullHome(Home):
    def get_template(self): 
        return 'webpage/full_home.html'
        #return 'webpage/fab_home.html'
    
    def extraCtx(self): 
        map_points = [sim_dict(x) for x in MapPoint.objects.all()]
        area = [sim_dict(x) for x in Area.objects.all()]
        page_item_list = [sim_dict(x) for x in MainPageItem.objects.all()]
        image_list =   [sim_dict(x) for x in PageImages.objects.all()]
        return {
            'map_points': map_points,
            'area_list': area,
            'page_item_list': page_item_list,
            'image_list': image_list,
        }
    
    def get_header_menu(self):
        return {}

class  OpenExe(Home): 
    def get_template(self): 
        return 'webpage/open_exe.html'


class ZhanShi(Home):
    def get_template(self): 
        return 'webpage/zhanshi.html'
    
    def extraCtx(self): 
        pageitems = [sim_dict(x) for x in ZhanRich.objects.filter(page = 'zhanshi').order_by('-priority', '-pk')]
        return {
            'crt_page_name':'zhanshi',
            'pageitems': pageitems,
        }


class PeiTao(ZhanShi):
    def extraCtx(self): 
        pageitems = [sim_dict(x) for x in ZhanRich.objects.filter(page = 'peitao').order_by('-priority', '-pk')]
        return {
            'crt_page_name':'peitao',
            'pageitems': pageitems,
        }

class Xuanchuan(Home):
    def get_template(self): 
        return 'webpage/zhanshi.html'
    
    def extraCtx(self): 
        pageitems = [sim_dict(x) for x in ZhanRich.objects.filter(page = 'xuanchuan').order_by('-priority', '-pk')]
        return {
            'crt_page_name':'xuanchuan',
            'pageitems': pageitems,
        } 

class Manual(ZhanShi):
    def extraCtx(self): 
        pageitems = [sim_dict(x) for x in ZhanRich.objects.filter(page = 'manual').order_by('-priority', '-pk')]
        return {
            'crt_page_name':'manual',
            'pageitems': pageitems,
        }     


class D3Wrap(Home):
    def get_template(self): 
        return 'webpage/3d_wrap.html'
    
    def extraCtx(self): 
        d3_url = self.request.GET.get('d3_url')
        return {
            'd3_url': d3_url,
        }

class D3WrapE(Home):
    def get_template(self): 
        return 'webpage/3d_wrap_e.html'
    
    def extraCtx(self): 
        d3_url = self.request.GET.get('d3_url')
        return {
            'd3_url': d3_url,
        }