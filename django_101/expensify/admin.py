from django.contrib import admin

# Register your models here.

from expensify.models import Transaction


admin.site.register(Transaction)
