from helpers.director.shortcut import ModelTable, TablePage, ModelFields, page_dc, director, RowFilter, RowSort
from .models import Building, FloorType, Floor

class BuildPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '楼'
    
    class tableCls(ModelTable):
        model = Building
        exclude = ['id']
        pop_edit_field = '_sequence'
        
        @classmethod
        def clean_search_args(cls, search_args): 
            if not search_args.get('_sort'):
                search_args['_sort'] = 'order'
            return search_args
        
        class sort(RowSort):
            names = ['order']
            
    
class BuildForm(ModelFields):
    class Meta:
        model = Building
        exclude = []

class FloorTypePage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '户型管理'
    
    class tableCls(ModelTable):
        pop_edit_field = '_sequence'
        model = FloorType
        exclude = ['id']

class FloorTypeForm(ModelFields):
    class Meta:
        model = FloorType
        exclude = []

class FloorPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '楼层管理'
    
    class tableCls(ModelTable):
        pop_edit_field = '_sequence'
        model = Floor
        exclude = ['id']
        
        def dict_head(self, head): 
            dc = {
                'floortype': 200,
            }
            if dc.get(head['name']):
                head['width'] = dc.get(head['name'])
            return head
        
        class filters(RowFilter):
            names = ['build', 'floortype']
        
        class sort(RowSort):
            names = ['order']

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