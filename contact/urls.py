
from django.conf.urls import patterns, include, url

from .views import ContactView


urlpatterns = [
    url(r'contact/$', ContactView.as_view(), name='go_contact'),
]
