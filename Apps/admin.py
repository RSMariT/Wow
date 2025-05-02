from django.contrib import admin

# Register your models here.
from .models import Insert,Update,Delete

admin.site.register(Insert)
admin.site.register(Update)
admin.site.register(Delete)