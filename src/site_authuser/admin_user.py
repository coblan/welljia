from helpers.director.shortcut import ModelTable, ModelFields, director, page_dc, TablePage
from django.contrib.auth.models import User
from usersystem.models import UserInfo

class UserAdminPage(TablePage):
    template = 'jb_admin/table.html'
    
    def get_label(self): 
        return '用户信息'
    
    class tableCls(ModelTable):
        model = User
        exclude = ['password', 'id', 'groups', 'user_permissions', 'is_superuser', 'first_name', 'last_name', ]
        #fields_sort = ['nickname', 'email', 'phone', ]
        def getExtraHead(self): 
            return [
                {'name': 'phone','label': '手机号',}, 
                {'name': 'nickname','label': '昵称',}
            ]
        
        def dict_row(self, inst): 
            if not hasattr(inst, 'userinfo'):
                UserInfo.objects.create(user = inst)
            user = inst
            return {
                'phone': user.userinfo.phone,
                'nickname': user.userinfo.nickname,
            }


director.update({
    'admin_user': UserAdminPage.tableCls,
    
})
page_dc.update({
    'admin_user': UserAdminPage,
})