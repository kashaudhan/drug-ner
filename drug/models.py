from django.db import models


class Drug(models.Model):
  sku_id = models.BigIntegerField(blank=True, null=True)
  product_id = models.BigIntegerField(blank=True, null=True)
  sku_name = models.CharField(max_length=256, blank=True, null=True)
  price = models.FloatField(blank=True, null=True)
  manufacturer_name = models.CharField(max_length=256, blank=True, null=True)
  salt_name = models.CharField(max_length=256, blank=True, null=True)
  drug_form = models.CharField(max_length=256, blank=True, null=True)
  pack_size = models.CharField(max_length=256, blank=True, null=True)
  strength = models.CharField(max_length=256, blank=True, null=True)
  product_banned_flag = models.BooleanField(blank=True, null=True)
  unit = models.CharField(max_length=256, blank=True, null=True)
  price_per_unit = models.FloatField(blank=True, null=True)

  def __str__(self):
      return f'{self.sku_name} ({self.salt_name})'
  
