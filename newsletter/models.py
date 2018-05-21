from django.db import models

from home.models import Country, Language


# Newsletter model
class Newsletter(models.Model):
    status = models.BooleanField(default=True)
    email = models.CharField(max_length=45)
    country = models.ForeignKey(Country)
    language = models.ForeignKey(Language)

    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.email