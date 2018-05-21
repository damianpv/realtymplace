from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import LanguageSerializer, StateSerializer, CountrySerializer, StatusSerializer, TypeSerializer, \
    PropertyBasicSerializer, PropertyBasicImageSerializer

from .views import AuthView
from home.models import Language, Country, State
from property.models import Basic, BasicImages, Status, Type


# API Rest for Language
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_fields = ('id_language', 'language', )


# API Rest for State
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_fields = ('id_state', 'country_id')


# API Rest for Country
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.filter(status=True)
    serializer_class = CountrySerializer
    filter_fields = ('id_country', )


# API Rest for Property-Basic
class PropertyBasicViewSet(viewsets.ModelViewSet):
    queryset = Basic.objects.all()
    serializer_class = PropertyBasicSerializer
    filter_fields = ('id', 'title', 'price', 'latitude', 'longitude', 'bedroom', 'bathroom', 'state', 'type', )


# API Rest for Property-Basic-Image
class PropertyBasicImageViewSet(viewsets.ModelViewSet):
    queryset = BasicImages.objects.all()
    serializer_class = PropertyBasicImageSerializer
    filter_fields = ('id', 'basic', )


# API Rest for Property-Status
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_fields = ('id', 'title', )


# API Rest for Property-Type
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_fields = ('id', 'title', )
