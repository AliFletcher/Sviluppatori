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
            form.save()
            return render(request, "home_page.html")

    return render(request, "sign_up.html", {'form': form})
