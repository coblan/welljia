from helpers.director.shortcut import TablePage, ModelTable, page_dc, director, ModelFields
from ..models import Area
class AreaPage(TablePage):
    def get_label(self): 
        return '区域设置'
    
    def get_template(self, prefer=None): 
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = Area
        exclude = ['id']
        pop_edit_field = 'label'
        

class AreaForm(ModelFields):
    class Meta:
        model = Area
        exclude = []

director.update({
    'Area': AreaPage.tableCls,
    'Area.edit': AreaForm,
    
})
page_dc.update({
    'Area': AreaPage,
})