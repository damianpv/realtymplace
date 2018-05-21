from django.db import models


# Language model
class Language(models.Model):
    id_language = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    language = models.CharField(max_length=30)
    code = models.CharField(max_length=5, blank=True)

    def __unicode__(self):
        return self.language


# Country model
class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    country = models.CharField(max_length=45)
    fips104 = models.CharField(max_length=7)
    iso2 = models.CharField(max_length=4)
    iso3 = models.CharField(max_length=4)
    ison = models.CharField(max_length=4)
    internet = models.CharField(max_length=8)
    capital = models.CharField(max_length=20)
    map_ref = models.CharField(max_length=50)
    nac_singular = models.CharField(max_length=30)
    nac_plural = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)
    currency_code = models.CharField(max_length=12)
    population = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)

    def __unicode__(self):
        return self.country


# State model
class State(models.Model):
    id_state = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    country = models.ForeignKey(Country)
    state = models.CharField(max_length=45)
    code = models.CharField(max_length=4)
    adm1code = models.CharField(max_length=8)

    def __unicode__(self):
        return self.state


# City model
class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    city = models.CharField(max_length=45)
    latitude = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.CharField(max_length=10, null=True, blank=True)
    timezone = models.CharField(max_length=10, null=True, blank=True)
    dmald = models.CharField(max_length=5, null=True, blank=True)
    code = models.CharField(max_length=6, null=True, blank=True)

    def __unicode__(self):
        return self.city
