from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitcoin_notifier_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'homePage.views.index'),
    url(r'^getCoinbasePrice/', 'getCoinbasePrice.views.index'),
    url(r'^getBitfinexPrice/', 'getBitfinexPrice.views.index'),
)
