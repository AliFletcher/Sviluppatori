from django.contrib.auth import login, authenticate
from django.shortcuts import render
from navbar import forms


# Create your views here.
def first_page(request):
    return render(request, "home_page.html")


def sign_up_page(request):
    form = forms.SignUpForm

    if request.method == "POST":
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return first_page(request)

    return render(request, "sign_up.html", {'form': form})


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return loged_in(request)
        else:
            return render(request, "login.html", {"error": True})
    else:
        return render(request, "login.html", {"error": False})


def loged_in(request):
    return render(request, "loged_in.html")


def contact_us(request):
    return render(request, "contact_us.html")


def contacted(request):
    return render(request, "contacted.html")
