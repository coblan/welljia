from helpers.director.shortcut import TablePage, ModelTable, page_dc, director, ModelFields
from ..models import MainPageItem
class MainPageItemPage(TablePage):
    def get_label(self): 
        return '主页设置'
    
    def get_template(self, prefer=None): 
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = MainPageItem
        exclude = ['id']
        pop_edit_field = 'label'
        

class MainPageForm(ModelFields):
    class Meta:
        model = MainPageItem
        exclude = []

director.update({
    'mainpage_cfg': MainPageItemPage.tableCls,
    'mainpage_cfg.edit': MainPageForm,
    
})
page_dc.update({
    'mainpage_cfg': MainPageItemPage,
})