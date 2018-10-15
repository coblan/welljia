from helpers.director.shortcut import ModelTable, TablePage, ModelFields, page_dc, director, RowFilter
from .models import Building, FloorType, Floor

class BuildPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '楼'
    
    class tableCls(ModelTable):
        model = Building
        exclude = []
        pop_edit_field = 'id'
    
class BuildForm(ModelFields):
    class Meta:
        model = Building
        exclude = []

class FloorTypePage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '户型管理'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = FloorType
        exclude = []

class FloorTypeForm(ModelFields):
    class Meta:
        model = FloorType
        exclude = []

class FloorPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '楼层管理'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = Floor
        exclude = []
        
        class filters(RowFilter):
            names = ['build', 'floortype']

class FloorForm(ModelFields):
    class Meta:
        model = Floor
        exclude = []


director.update({
    'building': BuildPage.tableCls,
    'building.edit': BuildForm,
    'floortype': FloorTypePage.tableCls,
    'floortype.edit': FloorTypeForm,
    'floor': FloorPage.tableCls,
    'floor.edit': FloorForm,
})

page_dc.update({
    'building': BuildPage,
    'floortype': FloorTypePage,
    'floor': FloorPage,
    
})