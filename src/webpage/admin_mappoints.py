from helpers.director.shortcut import TablePage, ModelTable, ModelFields, page_dc, director
from .models import MapPoint

class MapPointsPage(TablePage):
    def get_template(self, prefer=None): 
        return 'jb_admin/table.html'
    
    def get_label(self): 
        return '主页坐标点位'
    
    class tableCls(ModelTable):
        pop_edit_field = 'title'
        model = MapPoint
        exclude = ['id']

class MapPointForm(ModelFields):
    class Meta:
        model = MapPoint
        exclude = []
        

director.update({
    'MapPoint': MapPointsPage.tableCls,
    'MapPoint.edit': MapPointForm,
})

page_dc.update({
    'MapPoint': MapPointsPage,
})