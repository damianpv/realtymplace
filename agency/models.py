from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from home.models import Country, Language, State


# Agency model
class Agency(models.Model):
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=45, blank=True, null=True)
    cell = models.CharField(max_length=45, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    city = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.IntegerField(null=True)

    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    language = models.ForeignKey(Language)
    slug = models.SlugField(max_length=200, error_messages={'unique': 'Ya existe'})
    visit = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, related_name='agency_user')
    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.status = True
        self.slug = slugify(self.title)
        super(Agency, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('go_agency_detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    status = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=45, blank=True)
    subject = models.CharField(max_length=45, blank=True)
    message = models.TextField(blank=True)
    country = models.ForeignKey(Country, related_name='contact_country', null=True)
    language = models.ForeignKey(Language, related_name='contact_language', null=True)
    agency = models.ForeignKey(Agency)

    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return '%s - %s' % (self.name, self.email)

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super(Contact, self).save(*args, **kwargs)
