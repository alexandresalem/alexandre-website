from django.contrib import admin
from .models import Company, Article


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ['name']


@admin.register(Article)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ['date']
