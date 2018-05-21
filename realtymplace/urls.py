from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'pers_realtymplace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rmp_admin/', include(admin.site.urls)),

    url(r'accounts/', include('account_profile.urls')),
    url(r'', include('home.urls')),
    url(r'', include('contact.urls')),
    url(r'', include('agency.urls')),
    url(r'', include('property.urls')),
    url(r'', include('api.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

]
# urlpatterns += staticfiles_urlpatterns()
'''
if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT, }), )'''

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            url(r'^static/(?P<path>.*)$', 'serve'),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # uploaded media
    urlpatterns += staticfiles_urlpatterns()
