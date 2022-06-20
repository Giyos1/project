from django.contrib import admin
from .models import Deputy, Employee, Director

# Register your models here.

admin.site.register(Deputy)
admin.site.register(Director)
admin.site.register(Employee)
