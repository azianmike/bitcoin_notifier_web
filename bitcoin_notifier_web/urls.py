from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitcoin_notifier_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'homePage.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'homePage.views.index'),
    url(r'^getCoinbasePrice/', 'getCoinbasePrice.views.index'),
    url(r'^getBitfinexPrice/', 'getBitfinexPrice.views.index'),
    url(r'^registerJSON/', 'registerJSON.views.index'),
    url(r'^loginJSON/', 'loginJSON.views.index'),
    url(r'^checkIfLoggedInJSON/', 'loginJSON.views.checkIfLoggedIn'),
    url(r'^submitAlertJSON/', 'submitAlertJSON.views.index'),
    url(r'^home/', 'loginHome.views.index'),


)
