from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suplbizpj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'suplbizapp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/company_info/(?P<company_name>.*)', 'suplbizapp.views.company_info', name='company_info'),
    url(r'^search/', 'suplbizapp.views.search', name='search'),
)
