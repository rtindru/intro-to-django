from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello_django, name='hello_django'),
    url(r'^user/(?P<user>[\w]+)', views.hello_user, name='hello_user'),
    url(r'^template/(?P<user>[\w]+)', views.hello_template, name='hello_template'),
]
