from django.db import models

class Country(models.Model):
    iso_country_names_en = models.CharField(max_length=255)  
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    numeric_code = models.CharField(max_length=3)
    iso_3166_2 = models.CharField(max_length=13)

    class Meta:
        ordering = ['iso_country_names_en']
