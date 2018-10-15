from helpers.authuser.admin_regist import RegistFormPage
from helpers.authuser.base_data import auth_page_dc
from helpers.authuser.phone import make_phone_validate_code, validate_phone_code
from helpers.director.shortcut import director
from helpers.func.random_str import get_str
from django.utils import timezone
from usersystem.models import UserInfo
from django.contrib.auth.models import User
from django import forms
from helpers.third_interface.tencent_msg import send_validate_code

import logging
log = logging.getLogger('middle_result')

class SiteRegistFormPage(RegistFormPage):
    class fieldsCls(RegistFormPage.fieldsCls):
        field_sort = ['email', 'password', 'pswd2',  'phone', 'phone_code']
        def getExtraHeads(self): 
           
            return [
                {'name': 'pswd2','label': '确认密码','editor': 'password', 'required': True,'fv_rule': 'match(password)',}, 
                {'name': 'phone','label': '手机号','editor': 'number', 'required': True,'fv_rule': 'mobile',}, 
                {'name': 'phone_code','label': '验证码','editor': 'com-field-phone-code','required': True,
                 'phone_field': 'phone','fun': 'regist_send_phone_code',}
            ]
        
        def clean_dict(self, dc): 
            dc['username'] = "%s%s" % (get_str(6) , abs( hash(timezone.now) ))
            return dc
        
        def dict_head(self, head): 
            super().dict_head(head)
            if head['name'] == 'email':
                head['required'] = True
            return head
        
        #def clean_email(self):
            #email = self.cleaned_data.get('email')
            #if User.objects.filter(email=email).exists():
                #raise forms.ValidationError('该邮箱已经被申请')
            #return email
        
        def clean(self): 
            if 'pswd2' in self.cleaned_data:
                del self.cleaned_data['pswd2']            
            phone = self.kw.get('phone')
            phone_code = self.kw.get('phone_code')
            
            if UserInfo.objects.filter(phone = phone).exists():
                self._errors['phone'] = ['该手机已经被注册']
                return
            
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                self._errors['email'] = ('该邮箱已经被申请')
                return
            
            if not validate_phone_code(phone, phone_code):
                self._errors['phone_code'] = ['验证码不存在或者已经过期']
            return self.cleaned_data     
        
        def save_form(self): 
            super().save_form()
            user = self.instance
            #user.set_password(self.kw.get('password'))
            user.is_active=True
            user.save()
            UserInfo.objects.create(user = user, phone = self.kw.get('phone'))
        
    @staticmethod
    def send_phone_code(row): 
        code = make_phone_validate_code(row['phone'] )
        log.info('手机号:%(phone)s生成验证码%(code)s' % {'phone': row['phone'], 'code': code,})
        phone = row.get('phone')
        print(code)
        send_validate_code(phone, code)
        return {'row': row,}


director.update({
    'authuser.regist': SiteRegistFormPage.fieldsCls,
    'regist_send_phone_code': SiteRegistFormPage.send_phone_code,
})
        

auth_page_dc .update({
    'regist': SiteRegistFormPage,
})