from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import HomeView, PricingView, PrivacyPolicyView, TermsConditionsView, SitemapView

sitemaps = {
    'todos': SitemapView(),
}

# Privacy Policy
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='go_home'),
    url(r'^pricing/$', PricingView.as_view(), name='go_pricing'),
    url(r'^privacy-policy/$', PrivacyPolicyView.as_view(), name='go_privacy_policy'),
    url(r'^terms-conditions/$', TermsConditionsView.as_view(), name='go_terms_conditions'),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='seo/robots.txt'), name="robots"),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    # url(r'^google6114e44c796bd01e\.html$', TemplateView.as_view(template_name='seo/google6114e44c796bd01e.html'),
    # name="google6114e44c796bd01e"),
]
