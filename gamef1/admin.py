from django.contrib import admin
from .models import F1Prediction, Constructor
# Register your models here.


@admin.register(F1Prediction)
class F1GuesserAdmin(admin.ModelAdmin):
    pass


@admin.register(Constructor)
class ConstructorAdmin(admin.ModelAdmin):
    pass
