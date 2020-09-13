from django.contrib import admin
from .models import F1Prediction, Chassis
# Register your models here.


@admin.register(F1Prediction)
class F1GuesserAdmin(admin.ModelAdmin):
    pass


@admin.register(Chassis)
class ChassisAdmin(admin.ModelAdmin):
    list_display = ('chassis', 'constructor')
    pass
