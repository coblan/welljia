from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
PAGES = (
    ('zhanshi', '区域展示'), 
    #('peitao', '配套商业'), 
    ('xuanchuan', '品牌宣传'), 
    ('manual', '项目手册'), 
)
# Create your models here.
class ZhanRich(models.Model):
    menu_label = models.CharField('菜单显示名', max_length = 30, blank = True)
    label = models.CharField('大显示名', max_length = 30, blank = True, help_text = '显示位置，请参看demo页面')
    cover = PictureField('图片', max_length = 300, blank = True)
    page = models.CharField('从属页面',max_length = 30, blank = True, choices = PAGES)
    priority = models.IntegerField('优先级', default= 0, help_text= '大的排列在前')
    content = models.TextField('主要内容', blank= True)
    
class Building(models.Model):
    label = models.CharField('显示名', max_length = 30)
    order = models.IntegerField('顺序', default= 0, help_text= '排序，越小越前面')
    
    def __str__(self): 
        return self.label    

class FloorType(models.Model):
    label = models.CharField('户型名', max_length = 30)
    img_2d = PictureField('2D图片', blank = True, max_length = 300)
    img_3d = models.CharField('3D链接', blank = True, max_length = 300)
    
    def __str__(self): 
        return self.label

FLOOR_STATUS = (
    ('un_avaliable', '不可用'), 
    ('sold', '已售'), 
    ('avaliable', '可用')
)

class Floor(models.Model):
    label = models.CharField('显示名', max_length = 30)
    floortype = models.ForeignKey(FloorType, verbose_name = '户型')
    build = models.ForeignKey(Building, verbose_name = '栋', blank = True, null = True)
    status = models.CharField('状态', max_length = 30, choices = FLOOR_STATUS, default = 'un_avaliable')
    order = models.IntegerField('顺序', default= 0, help_text= '排序，越小越前面')
    
    def __str__(self): 
        return self.label
    
class MapPoint(models.Model):
    """一个建筑群"""
    title = models.CharField('显示名', max_length = 100)
    pos = models.CharField('坐标', max_length = 30, help_text = '请严格按照 x,y 的格式填写')
    url = models.CharField('3D资源地址', max_length = 200,blank=True,)
    
    def __str__(self): 
        return self.title

class Area(models.Model):
    label = models.CharField('显示名', max_length = 100)
    pos = models.CharField('坐标', max_length = 30, help_text = '请严格按照 x,y 的格式填写')
    pic =  PictureField('区域图', max_length = 300, blank = True)
    
    def __str__(self): 
        return self.label

class PageImages(models.Model):
    label = models.CharField('显示名', max_length = 100)
    pos = models.CharField('坐标', max_length = 30, help_text = '请严格按照 x,y 的格式填写')
    pic =  PictureField('区域图', max_length = 300, blank = True)
    link = models.CharField('链接',max_length = 300,blank=True)

class MainPageItem(models.Model):
    """ 表示一个 项目集合，一般包含多地 多个 楼群  """
    label =  models.CharField('显示名', max_length = 100)
    project = models.ManyToManyField(MapPoint, verbose_name = '项目点', blank = True)
    area = models.ManyToManyField(Area, verbose_name = '区域', blank = True)
    img_list = models.ManyToManyField(PageImages, verbose_name = '图片列表', blank = True)
    


    

    
    

    
