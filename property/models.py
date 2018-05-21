from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from home.models import Language, Country, State
from agency.models import Agency


# Type model / Aparment - House - ...
class Type(models.Model):
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=20)
    order = models.PositiveIntegerField()
    url_slug = models.SlugField(max_length=200, error_messages={'unique': "Ya existe."}, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.title


# Status model / Rent - Sale - ...
class Status(models.Model):
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=20)
    order = models.PositiveIntegerField()
    url_slug = models.SlugField(max_length=200, error_messages={'unique': "Ya existe."}, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.title


# Feature / 
class Feature(models.Model):
    status = models.BooleanField(default=False)

    title = models.CharField(max_length=50)
    order = models.PositiveIntegerField()
    url_slug = models.SlugField(max_length=200, error_messages={'unique': "Ya existe."}, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.title


# Basic model
class Basic(models.Model):
    active = models.BooleanField(default=False)

    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.ForeignKey(State, related_name='property_state')
    country = models.ForeignKey(Country, related_name='property_country')
    language = models.ForeignKey(Language, related_name='property_language')
    zip_code = models.IntegerField(null=True)

    type = models.ForeignKey(Type)  # department, house ...
    status = models.ForeignKey(Status)  # rent, sale ...

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    bedroom = models.PositiveIntegerField(default=0)
    bathroom = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    garage = models.PositiveIntegerField(default=0)
    allow_rating = models.BooleanField(default=0)

    feature = models.ManyToManyField(Feature)
    # video = models.FileField(max_length=255, upload_to='video/', blank=True)

    admin_comments = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, error_messages={'unique': "Ya existe."}, null=True, blank=True)
    visit = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, related_name='property_user')
    agency = models.ForeignKey(Agency, related_name='property_agency')
    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Basic, self).save(*args, **kwargs)

    def get_primary_image(self):
        get_first_image = BasicImages.objects.filter(basic=self.pk).first()
        return get_first_image

    def get_absolute_url(self):
        return reverse('go_property_detail', kwargs={'slug': self.slug})


class BasicImages(models.Model):
    active = models.BooleanField(default=True)

    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='property', null=True, blank=True)
    basic = models.ForeignKey(Basic)
    user = models.ForeignKey(User)
    order = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return unicode(self.image)
