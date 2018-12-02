from helpers.director.shortcut import TablePage, ModelFields, director, page_dc, ModelTable, RowFilter, RowSort
from .models import ZhanRich


class ZhanRichPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '富文本页面'
    
    class tableCls(ModelTable):
        model = ZhanRich
        exclude = ['id']
        hide_fields = ['content']
    
        def get_operation(self): 
            ops = super().get_operation()
            add_new =  ops[0]
            add_new.update({
                'tab_name': 'edit_form',
                'ctx_name': 'ZhanRichPageTabs',
            })
            return ops
        
        def dict_head(self, head): 
            if head['name'] == 'menu_label':
                head['editor'] = 'com-table-switch-to-tab'
                #head['inn_editor'] = 'com-table-sequence'
                head['tab_name'] = 'edit_form'
                head['ctx_name'] = 'ZhanRichPageTabs'
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
             'com':'com-tab-fields',
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
        ctx['named_ctx'] = {
            'ZhanRichPageTabs': ls,
        }
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