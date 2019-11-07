from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def first_page(request):
    return render(request, "first_page.html")
