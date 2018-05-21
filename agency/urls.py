
from django.conf.urls import patterns, include, url

from . import views


urlpatterns = [

    url(r'^agencies/$', views.AgenciesListView.as_view(), name='go_agency_list'),
    url(r'^agency/(?P<slug>.*)/$', views.AgencyDetailView.as_view(), name='go_agency_detail'),

    # ADMIN #

    url(r'^accounts/my-agency/$', views.MyAgencyListView.as_view(), name='go_my_agency_list'),
    url(r'^accounts/my-agency/(?P<pk>[\w]+)/delete/$', views.MyAgencyDeleteView.as_view(), name='go_my_agency_delete'),
    url(r'^accounts/my-agency/add/$', views.MyAgencyAddView.as_view(), name='go_my_agency_add'),
    url(r'^accounts/my-agency/add/success/$', views.PropertyAddSuccessView.as_view(), name='go_my_agency_add_success'),
    url(r'^accounts/my-agency/(?P<pk>[0-9]+)/edit/$', views.MyAgencyEditView.as_view(), name='go_my_agency_edit'),
    url(r'^accounts/my-agency/edit/success/$', views.MyAgencyEditSuccessView.as_view(),
        name='go_my_agency_edit_success'),

]
