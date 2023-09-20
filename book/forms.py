from django.contrib.auth.forms import AuthenticationForm
from hcaptcha.fields import hCaptchaField

class LoginForm(AuthenticationForm):
    hcaptcha = hCaptchaField(request=None)  # Pass the request argument manually

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(request, *args, **kwargs)
        self.fields['hcaptcha'].widget.request = request

# forms.py
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","national_number","phone_number",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)