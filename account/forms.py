from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

# from .validators import MyCustomPasswordValidator


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm new password', widget=forms.PasswordInput)

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        MyCustomPasswordValidator().validate(new_password)
        return new_password

    def confirm_password(self):
        new_password = self.cleaned_data.get('new_password1')
        confirm_new_password = self.cleaned_data.get('new_password2')
        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise ValidationError('The two new password fields must match.')
        return confirm_new_password

    def save(self, commit=True):
        password = self.cleaned_data['new_password']
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
