from django import forms
from django.contrib.auth.forms import User
from navbar.models import Course


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password mismatch!")
        return password2

    def save(self, commit=True):
        user = super(forms.ModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EditForm(forms.Form):
    first_name = forms.CharField(max_length=264, required=False)
    last_name = forms.CharField(max_length=264, required=False)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
