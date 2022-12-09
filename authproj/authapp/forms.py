from django import forms

class register_form(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    email= forms.EmailField(label = 'email', max_length=100)
    password1 = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput())



class login_form(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password1 = forms.CharField(widget = forms.PasswordInput(), label='password')