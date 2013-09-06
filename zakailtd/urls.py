from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.conf.urls.defaults import *
import settings





# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^zakai/$' , 'zakai.views.index'),


    url(r'^catalog/$' , 'zakai.views.view_catalogs'),
    url(r'^catalog/(?P<slug>.*)/$' , 'zakai.views.view_catalog'),


    #url(r'^(?P<url>profile/)$', 'django.contrib.flatpages.views.flatpage'),

    
    #for a 127.0.0.1:8000
    (r'^$', 'zakai.views.index'),
#    (r'^products/$', 'zakai.views.ProductsAll'),
    (r'^product/(?P<slug>.+)/$', 'zakai.views.view_product'),
#    (r'^products/(?P<productslug>[-\w]+)/$', 'zakai.views.SpecificProduct'),
	

    # url(r'^zakailtd/', include('zakailtd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', "django.contrib.staticfiles.views.serve", {'document_root': settings.STATIC_ROOT}),

    (r'^media/(?P<path>.*)$', "django.contrib.staticfiles.views.serve", {'document_root': settings.MEDIA_ROOT}),


)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )