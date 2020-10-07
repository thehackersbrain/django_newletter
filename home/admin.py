from django.contrib import admin
from .models import Newsletters


# Register your models here.


class Newsletter_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_date']


admin.site.register(Newsletters, Newsletter_admin)
