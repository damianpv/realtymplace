from django.db import models

from home.models import Country, Language


# Contact model
class Contact(models.Model):
    status = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    agency = models.CharField(max_length=100, blank=True)
    how_know_us = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=45, blank=True)
    message = models.TextField(blank=True)
    country = models.ForeignKey(Country, null=True)
    language = models.ForeignKey(Language, null=True)

    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)
