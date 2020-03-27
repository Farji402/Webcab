from django import forms
from signup.models import Janta


class login_form(forms.Form):
    outlook_id = forms.CharField(max_length=20)
    pwd = forms.CharField(max_length=30)
    widget = {
        'pwd': forms.PasswordInput
    }

    def clean_outlook_id(self):
        outlook = self.cleaned_data.get("outlook_id")
        dbuser = Janta.objects.filter(outlook_id=outlook)

        if not dbuser:
            raise forms.ValidationError("User does not exists!")

    def clean_pwd(self):
        passwd = self.cleaned_data.get("pwd")
        dbuser = Janta.objects.filter(password=passwd)

        if not dbuser:
            raise forms.ValidationError("User does not exists!")




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['outlook_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['outlook_id'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['outlook_id'].widget.attrs.update({'id': 'email'})
        self.fields['pwd'].widget.attrs.update({'class': 'form-control'})
        self.fields['pwd'].widget.attrs.update({'placeholder': 'Enter Password'})
        self.fields['pwd'].widget.attrs.update({'id': 'pwd'})

class form_edit_general(forms.Form):
    username = forms.CharField(max_length = 30)
    phone = forms.CharField(max_length = 10)

class form_edit_security(forms.Form):
    current_password = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)
    widget = {
        'password': forms.PasswordInput,
        'current_password': forms.PasswordInput
    }

class form_dp(forms.Form):
    dp = forms.ImageField()

