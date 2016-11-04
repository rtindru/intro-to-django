from django.conf.urls import url, include

from expensify import views

urlpatterns = [
    url(r'transactions/', views.transaction_list, name='transaction_list'),
    url(r'add/', views.transaction_form),
]
