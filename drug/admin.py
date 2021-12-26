from django.contrib import admin, messages
from django.http.response import HttpResponseRedirect
import pandas as pd
from django import forms
from django.urls import path, reverse
from django.shortcuts import render
from .models import *


class CSVImportFrom(forms.Form):
    csv_upload = forms.FileField()


class DrugAdmin(admin.ModelAdmin):
  list_display = ('id', 'sku_id', 'product_id', 'sku_name', 'price', 'manufacturer_name', 'salt_name', 'drug_form', 'pack_size', 'strength', 'product_banned_flag', 'unit', 'price_per_unit')

  def get_urls(self):
    urls = super().get_urls()
    new_urls = [path('upload-csv/', self.upload_csv),]
    return new_urls + urls

  def upload_csv(self, request):
    if request.method == 'POST':
      csv_file = request.FILES["csv_upload"]

      if not csv_file.name.endswith('.csv'):
        messages.warning(request, "Wrong file type uploaded")
        return HttpResponseRedirect(request.path_info)

      df = pd.read_excel(csv_file)
      for i in range(len(df)):
        sku_id = None if df.iloc[i, 0] == '-' else df.iloc[i, 0]
        product_id = None if df.iloc[i, 1] == '-' else df.iloc[i, 1]
        sku_name = None if df.iloc[i, 2] == '-' else df.iloc[i, 2]
        price = None if df.iloc[i, 3] == '-' else df.iloc[i, 3]
        manufacturer_name = None if df.iloc[i, 4] == '-' else df.iloc[i, 4]
        salt_name = None if df.iloc[i, 5] == '-' else df.iloc[i, 5]
        drug_form = None if df.iloc[i, 6] == '-' else df.iloc[i, 6]
        pack_size = None if df.iloc[i, 7] == '-' else df.iloc[i, 7]
        strength = None if df.iloc[i, 8] == '-' else df.iloc[i, 8]
        product_banned_flag = None 
        if df.iloc[i, 9] == '-':
          product_banned_flag = None
        elif df.iloc[i, 9]=='FALSE':
          product_banned_flag = False
        else:
          product_banned_flag = True
        
        unit = None if df.iloc[i, 10] == '-' else df.iloc[i, 10]
        price_per_unit = None if df.iloc[i, 11] == '-' else df.iloc[i, 11]

        Drug.objects.update_or_create(
          sku_id=sku_id, 
          product_id=product_id, 
          sku_name=sku_name, 
          price=price, 
          manufacturer_name=manufacturer_name,
          salt_name=salt_name,
          drug_form=drug_form,
          pack_size=pack_size,
          strength=strength,
          product_banned_flag=product_banned_flag,
          unit=unit,
          price_per_unit=price_per_unit
        )

      url = reverse('admin:index')
      return HttpResponseRedirect(url)

    form = CSVImportFrom()
    data = {'form': form}
    return render(request, 'admin/csv_upload.html', data)

admin.site.register(Drug, DrugAdmin)