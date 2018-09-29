from helpers.director.shortcut import  Fields, page_dc, director, FieldsPage
from helpers.director.kv import get_value, set_value

class LinkForm(FieldsPage):
    template = 'jb_admin/fields.html'
    def get_label(self): 
        return '链接编辑'
    
    class fieldsCls(Fields):
        def get_heads(self): 
            return [
                {'name': 'sha_pan_link', 'label': '数字沙盘','editor': 'linetext','style': 'width:300px',}, 
                {'name': 'huxing_link','label': '户型鉴赏','editor': 'linetext','style': 'width:300px',}, 
            ]
        
        def get_row(self): 
            return {
                'sha_pan_link': get_value('sha_pan_link'),
                'huxing_link': get_value('huxing_link'),
                '_director_name': self.get_director_name(),
            }
        
        def save_form(self): 
            ls = ['sha_pan_link', 'huxing_link', ]
            for k, v in self.kw.items():
                if k in ls and v:
                    set_value(k, v)


director.update({
    'link_form': LinkForm.fieldsCls,
})

page_dc.update({
    'link_form': LinkForm,
})

