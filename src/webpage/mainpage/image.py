from helpers.director.shortcut import TablePage, ModelTable, page_dc, director, ModelFields
from ..models import PageImages
class ImagePage(TablePage):
    def get_label(self): 
        return '区域设置'
    
    def get_template(self, prefer=None): 
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = PageImages
        exclude = ['id']
        pop_edit_field = 'label'
        

class ImageForm(ModelFields):
    class Meta:
        model = PageImages
        exclude = []

director.update({
    'image_list': ImagePage.tableCls,
    'image_list.edit':ImageForm,
    
})
page_dc.update({
    'image_list': ImagePage,
})