
from django.conf.urls import patterns, include, url
from rest_framework import routers

from .viewsets import LanguageViewSet, StateViewSet, CountryViewSet, AuthView, PropertyBasicViewSet, \
    PropertyBasicImageViewSet, StatusViewSet, TypeViewSet
# UserViewSet, , FriendViewSet

router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'state', StateViewSet)
router.register(r'country', CountryViewSet)
router.register(r'status', StatusViewSet)
router.register(r'type', TypeViewSet)

router.register(r'property-basic', PropertyBasicViewSet)
router.register(r'property-basic-images', PropertyBasicImageViewSet)

urlpatterns = [
    url(r'^api/v1.0/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/$', AuthView.as_view(), name='authenticate'),
]
