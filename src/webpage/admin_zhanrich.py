from helpers.director.shortcut import TablePage, ModelFields, director, page_dc, ModelTable, RowFilter, RowSort
from .models import ZhanRich


class ZhanRichPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '单页面管理'
    
    class tableCls(ModelTable):
        model = ZhanRich
        exclude = []
        hide_fields = ['content']
    
        def get_operation(self): 
            ops = super().get_operation()
            ops[0]['tab_name'] = 'edit_form'
            return ops
        def dict_head(self, head): 
            if head['name'] == 'id':
                head['editor'] = 'com-table-switch-to-tab'
                head['tab_name'] = 'edit_form'
            return head
        
        class filters(RowFilter):
            names = ['page']
        
        class sort(RowSort):
            names = ['priority']
        
    def get_context(self): 
        ctx = super().get_context()
        form_obj = ZhanForm(crt_user= self.crt_user)
        ls = [
            {'name':'edit_form',
             'label':'基本信息',
             'com':'com_tab_fields',
             'get_data':{
                 'fun':'get_row',
                 'kws':{
                    'director_name':form_obj.get_director_name(),
                    'relat_field':'pk',              
                 }
             },
             'after_save':{
                 'fun':'update_or_insert'
                 #'fun':'do_nothing'
                 #'fun':'update_par_row_from_db'
             },
             'heads': form_obj.get_heads(),
             'ops': form_obj.get_operations()                 
             }, 
        ]
        ctx['tabs'] = ls
        return ctx

class ZhanForm(ModelFields):
    class Meta:
        model = ZhanRich
        exclude = []
    
    def dict_head(self, head): 
        if head['name'] == 'content':
            head['editor'] = 'richtext'
            #head['set'] = 'complex'
        return head



director.update({
    'ZhanRichPage': ZhanRichPage.tableCls,
    'ZhanRichPage.edit': ZhanForm,
})

page_dc.update({
    'ZhanRichPage': ZhanRichPage,
})