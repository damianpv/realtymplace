#from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.sitemaps import Sitemap
from django.conf import settings
from braces.views import LoginRequiredMixin

from property.models import Basic


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        # TODO: Filtrar por fecha de actualizacion
        context['property_recent'] = Basic.objects.all().order_by('-pk')[:4]
        context['property_important'] = Basic.objects.all().order_by('-visit')[:4]  # More visited.
        context['static_url'] = settings.STATIC_URL
        context['site_url'] = settings.SITE_URL

        return context


class PricingView(TemplateView):
    template_name = 'home/pricing.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'home/privacy_policy.html'


class TermsConditionsView(TemplateView):
    template_name = 'home/terms_conditions.html'


class SitemapView(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Basic.objects.filter(active=True)
