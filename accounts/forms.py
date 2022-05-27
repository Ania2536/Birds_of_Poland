from django import forms

class RegisterFormView(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))

class LoginFormView(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))