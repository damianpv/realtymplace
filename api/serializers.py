from rest_framework import serializers
from django.contrib.auth.models import User

from home.models import Language, State, Country
from property.models import Basic, BasicImages, Status, Type

################### HOME #########################


# Language
class LanguageSerializer(serializers.ModelSerializer):
    property_language = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='basic-detail')

    class Meta:
        model = Language
        fields = ('id_language', 'language', 'property_language', )

# State
class StateSerializer(serializers.ModelSerializer):
    property_state = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='basic-detail')

    class Meta:
        model = State
        fields = ('id_state', 'state', 'property_state', )

# Country
class CountrySerializer(serializers.ModelSerializer):
    property_country = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='basic-detail')

    class Meta:
        model = Country
        fields = ('id_country', 'country', 'property_country', )


################### Property #########################

class PropertyBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basic
        fields = ('id', 'title', 'price', 'description', 'address', 'city', 'state', 'country', 'language', 'zip_code',
                  'type', 'status', 'latitude', 'longitude', 'bedroom', 'bathroom', 'area', 'garage', 'allow_rating',
                  'feature', 'agency', 'slug', )


class PropertyBasicImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasicImages
        fields = ('id', 'title', 'image', )


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'title', 'order', 'url_slug', )


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'title', 'order', 'url_slug', )
