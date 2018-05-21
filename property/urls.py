
from django.conf.urls import patterns, include, url

from . import views


urlpatterns = [

    url(r'^property/$', views.PropertyListView.as_view(), name='go_property_list'),
    url(r'^property/(?P<slug>.*)/$', views.PropertyDetailView.as_view(), name='go_property_detail'),

    # ADMIN #

    url(r'^accounts/my-property/$', views.MyPropertiesListView.as_view(), name='go_my_property_list'),
    url(r'^accounts/my-property/(?P<pk>[\w]+)/delete/$', views.MyPropertiesDeleteView.as_view(),
        name='go_my_properties_delete'),
    url(r'^accounts/my-property/add/$', views.PropertyAddView.as_view(), name='go_property_add'),
    url(r'^accounts/my-property/add-images/(?P<pk>[\w]+)/$', views.PropertyAddImagesView.as_view(),
        name='go_property_add_images'),
    url(r'^accounts/my-property/add/success/$', views.PropertyCreatedSuccessView.as_view(),
        name='go_property_add_success'),
    url(r'^accounts/my-property/(?P<pk>[0-9]+)/update/$', views.PropertyUpdateView.as_view(),
        name='go_my_property_update'),
    url(r'^accounts/my-property/update/success/$', views.PropertyUpdatedSuccessView.as_view(),
        name='go_property_updated_success'),

    # url(r'^', include('multiuploader.urls')),
]
