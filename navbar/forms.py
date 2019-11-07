from django import forms
from navbar.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
