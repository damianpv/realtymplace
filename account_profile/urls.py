
from django.conf.urls import patterns, include, url

# from home.views import NamedUrlRedirectView
from .views import ProfileView, BookmarkedView, BookmarkedAjaxView

urlpatterns = [
    # url(r'^$', NamedUrlRedirectView.as_view(url='go_profile'), name='go_profile_redirect'),
    url(r'^profile/$', ProfileView.as_view(), name='go_profile'),

    url(r'^bookmarked/$', BookmarkedView.as_view(), name='go_my_bookmarked_list'),
    url(r'^bookmarked_ajax/$', BookmarkedAjaxView.as_view(), name='go_my_bookmarked_ajax'),

]
