from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('apps.hello.urls')),
    url(r'^admin/', include(admin.site.urls), name="admin"),
)
urlpatterns += staticfiles_urlpatterns()
