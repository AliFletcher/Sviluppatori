from django.conf.urls import url

from navbar import views

urlpatterns = [
    url(r'^$', views.first_page, name="first_page"),
    url(r'^sign_up/$', views.sign_up_page, name="sign_up")
]
