from django import forms

class registerForm(forms.Form):
    username=forms.CharField(max_length=200)
    email=forms.EmailField()
    password=forms.CharField(max_length=200 ,widget=forms.PasswordInput)
class loginForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)