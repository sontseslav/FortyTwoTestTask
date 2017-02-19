from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.hello.views import IndexView, RequestsView

urlpatterns = patterns(
    '',
    url(r'^requests$', RequestsView.as_view(), name="requests"),
    url(r'^$', IndexView.as_view(), name="index"),
)
urlpatterns += staticfiles_urlpatterns()
