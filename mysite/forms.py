#_*_ encoding: utf-8 *_*
from django import forms
from mysite import models
from captcha.fields import CaptchaField
from django.forms import ModelForm
from django.contrib.auth.models import User

class PollForm(ModelForm):
    class Meta:
        model = models.Poll
        fields = ['name', 'enabled']
    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '標題'
        self.fields['enabled'].label = '啟用'

class PollItemForm(ModelForm):
    class Meta:
        model = models.PollItem
        fields = ['name', 'image_url', 'vote']
    def __init__(self, *args, **kwargs):
        super(PollItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '選項名稱'
        self.fields['image_url'].label = '圖片網址'
        self.fields['vote'].label = '起始票數'

class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ['height', 'male', 'website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高(cm)'
        self.fields['male'].label = '是男生嗎'
        self.fields['website'].label = '個人網站'


class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())

class DateInput2(forms.DateInput):
    input_type = 'date'

class DiaryForm(ModelForm):

    class Meta:
        model = models.Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        """
        widgets = {
            'ddate': forms.DateInput(input_formats='%m/%d/%Y')
        }
        """

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花費(元)'
        self.fields['weight'].label = '今日體重(KG)'
        self.fields['note'].label = '心情留言'
        self.fields['ddate'].label = '日期'
"""
class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在學', required=False)
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)
    
class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '你的暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'
        self.fields['captcha'].label = '確定你不是機器人'
"""