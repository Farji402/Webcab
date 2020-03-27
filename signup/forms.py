from django import forms
from .models import Janta

class JantaForm(forms.ModelForm):

    class Meta:
        model = Janta
        fields = ['outlook_id', 'user_name', 'password', 'mob', 'gender']
        widgets = {
            'gender': forms.RadioSelect,
            'password': forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['outlook_id'].widget.attrs.update({'class': 'form-control '})
        self.fields['outlook_id'].widget.attrs.update({'placeholder': 'Outlook ID'})
        self.fields['user_name'].widget.attrs.update({'class': 'form-control rounded'})
        self.fields['user_name'].widget.attrs.update({'placeholder': 'User name'})
        self.fields['password'].widget.attrs.update({'class': 'form-control rounded'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['mob'].widget.attrs.update({'class': 'form-control rounded'})
        self.fields['mob'].widget.attrs.update({'placeholder': 'Phone No.'})
        self.fields['gender'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['gender'].widget.attrs.update({'class': 'required'})


