from django.views.generic.base import TemplateView
from django.http import Http404
from apps.hello.models import Person


class IndexView(TemplateView):
    template_name = 'hello/index.html'
    model = Person
    content = None

    def get(self, request, *args, **kwargs):
        try:
            self.content = Person.objects.get(pk=1)
        except KeyError:
            raise Http404
        return super(IndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super(IndexView, self).get_context_data(**kwargs)
        content['person'] = self.content
        return content
