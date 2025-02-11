from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Tai khoan", max_length=255)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mat khau", widget = forms.PasswordInput() , max_length=255)
    confirm_password = forms.CharField(label="Nhap lai mat khau", widget = forms.PasswordInput() , max_length=255)

    def clean_confirm_password(self):
        if "password" in self.cleaned_data:
            password = self.cleaned_data["password"]
            confirm_password = self.cleaned_data["confirm_password"]
            if password == confirm_password and password:
                return confirm_password
        raise forms.ValidationError("Mat khau khong hop le !")
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r"^\w+$", username):
            raise forms.ValidationError("Ten tai khoan chua ki tu dac biet !")   
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tai khoan da ton tai !")
    
    def save(self):
        User.objects.create_user(username= self.cleaned_data["username"], email= self.cleaned_data["email"], password= self.cleaned_data["password"])