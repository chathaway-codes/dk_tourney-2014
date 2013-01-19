from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from rest_api.apis import raw
import tournament.urls
from tournament.views import TournamentListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name="home.html")), {}, 'home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tournament/', include(tournament.urls)),

    # Registration URL
#    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Login URL
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'home.html'}),

    # REST API
    url(r'^api/', include(raw.api.urls)),
    url(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
