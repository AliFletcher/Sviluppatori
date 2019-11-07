from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def first_page(request):
    return render(request, "home_page.html")


def sign_up_page(request):
    return render(request, "sign_up.html")
