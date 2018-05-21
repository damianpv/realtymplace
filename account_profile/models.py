from django.db import models
from django.contrib.auth.models import User

from property.models import Basic


# Bookmark model
class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmark_user')
    property = models.ForeignKey(Basic, related_name='bookmark_property')

    created_at = models.DateTimeField(auto_now_add=True)    # set when it's created
    updated_at = models.DateTimeField(auto_now=True)        # set every time it's updated

    def __unicode__(self):
        return self.property.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    about_me = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    account_tw = models.CharField(max_length=45, null=True, blank=True)
    account_fb = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

    def __unicode__(self):
        return self.user.email
