from django.contrib import admin
from .models import Uygulama


@admin.register(Uygulama)
class UygulamaAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name',)
