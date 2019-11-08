from django import forms
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from navbar import forms
from django.contrib.auth.decorators import login_required
from navbar.models import Course


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
    if request.method == "POST":
        if 250 < len(request.POST['text']) or len(request.POST['text']) < 10:
            return render(request, "contact_us.html")
        # send_mail(
        #     request.POST['title'],
        #     request.POST['email'] + '\n' + request.POST['text'],
        #     'a.a.ghanati@gmail.com',
        #     ['webe19lopers@gmail.com', 'a.a.ghanati@gmail.com']
        # )
        return redirect("/contacted/")
    return render(request, "contact_us.html")


def contacted(request):
    return render(request, "contacted.html")


@login_required(login_url='/')
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
        if request.POST['first_name'] != '':
            request.user.first_name = request.POST['first_name']
        if request.POST['last_name'] != '':
            request.user.last_name = request.POST['last_name']
        request.user.save()
        return profile(request)
    return render(request, "user_edit.html", {"form": form})


@login_required(login_url='/')
def createcourse(request):
    form = forms.CourseForm
    if request.method == "POST":
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request, "createcourse.html", {'form':form})


@login_required(login_url='/')
def showcourse(request):
    course_list = Course.objects.order_by('name')
    return render(request, 'showcourse.html', context={'course_list':course_list})

