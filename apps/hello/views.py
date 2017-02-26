from django.http import Http404
from django.views.generic.base import TemplateView
from apps.hello.models import Person


class IndexView(TemplateView):
    pass