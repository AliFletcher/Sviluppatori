from django.shortcuts import render
from navbar import forms
from django.contrib.auth import authenticate, login


# Create your views here.
def first_page(request):
    return render(request, "home_page.html")


def sign_up_page(request):
    form = forms.SignUpForm

    if request.method == "POST":
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            return first_page(request)

    return render(request, "sign_up.html", {'form': form})


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        return render(request, "login.html", {'message': 'invalid password or username'})
