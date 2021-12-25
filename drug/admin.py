from django.contrib import admin
from .models import *

class DrugAdmin(admin.ModelAdmin):
  list_display = ('id', 'sku_id', 'product_id', 'sku_name', 'price', 'manufacturer_name', 'salt_name')

admin.site.register(Drug, DrugAdmin)