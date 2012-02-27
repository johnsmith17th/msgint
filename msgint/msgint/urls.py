from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'msgint.views.msg_list'),
    url(r'^spam/$', 'msgint.views.msg_spam'),
    url(r'^normal/$', 'msgint.views.msg_normal'),
    url(r'^add/$', 'msgint.views.msg_add'),
    url(r'^del/$', 'msgint.views.msg_del'),
    url(r'^seg/(?P<pk>\d+)/$', 'msgint.views.msg_seg'),
    # Examples:
    # url(r'^$', 'msgint.views.home', name='home'),
    # url(r'^msgint/', include('msgint.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
