from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
PAGES = (
    ('zhanshi', '区域展示'), 
    ('xuanchuan', '品牌宣传')
)
# Create your models here.
class ZhanRich(models.Model):
    menu_label = models.CharField('菜单显示名', max_length = 30, blank = True)
    label = models.CharField('大显示名', max_length = 30, blank = True)
    cover = PictureField('图片', max_length = 300, blank = True)
    content = models.TextField('主要内容', blank= True)
    page = models.CharField('从属页面',max_length = 30, blank = True, choices = PAGES)
    
