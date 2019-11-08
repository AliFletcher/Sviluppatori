from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from navbar import forms
from django.contrib.auth.decorators import login_required


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
        else:
            try:
                User.objects.get(username=form.cleaned_data['username'])
            except KeyError:
                return render(request, "sign_up.html", {'form': form, "error": 2})
            except User.DoesNotExist:
                pass
            return render(request, "sign_up.html", {'form': form, "error": 1})

    return render(request, "sign_up.html", {'form': form, "error": 0})


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": True})
    else:
        return render(request, "login.html", {"error": False})


def contact_us(request):
    return render(request, "contact_us.html")


def contacted(request):
    if request.method == "POST":
        send_mail(
            request.POST['title'],
            request.POST['email'] + '\n' + request.POST['text'],
            'a.a.ghanati@gmail.com',
            ['webe19lopers@gmail.com'],
            fail_silently=False,
        )
    return render(request, "contacted.html")


def log_out(request):
    logout(request)
    return redirect("/")


def panel(request):
    return render(request, "panel.html")


@login_required(login_url='/')
def profile(request):
    return render(request, "profile.html", {"first_name": request.user.first_name, "last_name": request.user.last_name, "username": request.user.username})


@login_required(login_url='/')
def user_edit(request):
    form = forms.EditForm
    if request.method == "POST":
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        return profile(request)
    return render(request, "user_edit.html", {"form": form})
