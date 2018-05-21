# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django import template
from django.contrib.auth.models import User
from property.models import Basic
from django.conf import settings

from home.models import Country, State
from account_profile.models import Bookmark
from agency.models import Agency


def processor_language(request):
    # Default language: ES
    from django.utils import translation
    translation.activate("es")

    return ''


def processor_location(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')

    # client_ip = '98.208.227.146'  # TODO: Delete it

    import geoip2.webservice

    try:
        client = geoip2.webservice.Client(settings.MAXMINDID, settings.MAXMINDKEY)

        response = client.city(client_ip)

        # VALUES
        location_status = 1

        location_country_code = response.country.iso_code
        location_country = response.country.name
        location_country_geoid = response.country.geoname_id

        location_latitude = response.location.latitude
        location_longitude = response.location.longitude
        location_time_zone = response.location.time_zone

        location_state_code = response.subdivisions.most_specific.iso_code
        location_state = response.subdivisions.most_specific.name
        location_state_geoid = response.subdivisions.most_specific.geoname_id

        location_city = response.city.name
        location_city_geoid = response.city.geoname_id

        location_queries_remaining = response.maxmind.queries_remaining

    except:
        # VALUES
        location_status = 0

        location_country_code = ''
        location_country = ''
        location_country_geoid = ''

        location_latitude = ''
        location_longitude = ''
        location_time_zone = ''

        location_state_code = ''
        location_state = ''
        location_state_geoid = ''

        location_city = ''
        location_city_geoid = ''

        location_queries_remaining = 0

    try:
        # get our Country pk
        country = Country.objects.filter(iso2=location_country_code)[0]
        country_pk = country.pk
    except:
        country_pk = 159

    try:
        # get our State pk
        state = State.objects.filter(code=location_state_code)[0]
        state_pk = state.pk
    except:
        state_pk = 59

    context = {
        'location_status': location_status,
        'location_country_pk': country_pk,
        'location_state_pk': state_pk,
        # country
        'location_country_code': location_country_code,
        'location_country': location_country,
        'location_country_geoid': location_country_geoid,
        # location
        'location_latitude': location_latitude,
        'location_longitude': location_longitude,
        'location_time_zone': location_time_zone,
        # subdivisions / state
        'location_state_code': location_state_code,
        'location_state': location_state,
        'location_state_geoid': location_state_geoid,
        # city
        'location_city': location_city,
        'location_city_geoid': location_city_geoid,
        # maxmind queries
        'location_queries_remaining': location_queries_remaining,
    }

    # print 'Quedan: %s queries' % location_queries_remaining

    return context


def processor_username(request):

    first_name = property_num = bookmark_num = agency_num = ''
    if request.user.is_authenticated():
        # User
        user = User.objects.get(pk=request.user.id)
        first_name = user.first_name
        # Properties Total
        property_num = Basic.objects.filter(user=request.user).count()
        # Bookmarked Total
        bookmark_num = Bookmark.objects.filter(user=request.user).count()
        # Agencies Total
        agency_num = Agency.objects.filter(user=request.user).count()


    context = {
        'first_name': first_name,
        'property_num': property_num,
        'bookmark_num': bookmark_num,
        'agency_num': agency_num,
    }
    return context


def processor_recent_property(request):
    # import locale
    # locale.setlocale(locale.LC_ALL, 'es_ES')

    recent_footer_list = Basic.objects.filter(active=True).order_by('-pk')[:2]

    context = {
        'CONST_TWITTER': settings.CONSTANCE['TWITTER'],
        'CONST_FACEBOOK': settings.CONSTANCE['FACEBOOK'],

        'recent_footer_list': recent_footer_list,
    }
    return context


def processor_featured_properties(request):

    p_location = processor_location(request)  # context processor

    featured_list = Basic.objects.filter(active=True).order_by('-pk')[:10]
    featured_list_footer = Basic.objects.all().order_by('-visit')[:2]

    context = {
        'processor_location': p_location['location_country_code'],
        'featured_list': featured_list,
        'featured_list_footer': featured_list_footer,
    }
    # import pprint
    # pprint.pprint(context)

    return context


def function(request):
    return 'testing'
