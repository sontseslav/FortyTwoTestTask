from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.hello.views import IndexView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name="index"),
)
urlpatterns += staticfiles_urlpatterns()
