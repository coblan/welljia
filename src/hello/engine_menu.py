# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine,page,fa,can_list,can_touch
from django.contrib.auth.models import User,Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp
from django.utils.translation import ugettext as _
from django.conf import settings


class PcMenu(BaseEngine):
    url_name='admin'
    #brand = 'SportsCenter'
    #mini_brand='SC'
    brand = '管理后台'
    mini_brand='管理' 
    

    @property
    def menu(self):
        crt_user = self.request.user
        menu=[
            {'label':_('DashBoard'),'url':page('home'),'icon':fa('fa-home'), 'visible':True}, 
            
            
            {'label':_('用户管理'),'icon':fa('fa-home'), 'visible':True,'submenu':[
                {'label':'用户信息','url':page('admin_user'),'visible':can_touch(User, crt_user)},
                ]}, 
            
            #{'label':_('cms管理'),'url':page('simcms.page'),'icon':fa('fa-home'), 'visible':True}, 

 
            {'label':_('User'),'icon':fa('fa-user'),'visible':True,
                 'submenu':[
                     {'label':_('Account'),'url':page('jb_user'),'visible':can_touch(User, crt_user)},
                     {'label':_('权限组'),'url':page('jb_group'),'visible':can_touch(Group, crt_user)},
                     #{'label':'权限分组','url':page('group_human'),'visible':can_touch(Group)},
                   ]},   
            ]
        return menu

PcMenu.add_pages(page_dc)