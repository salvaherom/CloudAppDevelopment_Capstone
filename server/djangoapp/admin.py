from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'dealerid', 'carmake', 'type', 'year'] 

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    field = ['name', 'description']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)