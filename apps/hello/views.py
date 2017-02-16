from django.views.generic.base import TemplateView
from django.http import Http404
from apps.hello.models import Person


class IndexView(TemplateView):
    template_name = 'index.html'
    model = Person
    content = None

    def get(self, request, *args, **kwargs):
        try:
            self.content = Person.objects.get(pk=1)
        except KeyError:
            # use template
            raise Http404
        return super(IndexView, self).get(request, *args, **kwargs)

    def context(self, **kwargs):
        context = super(IndexView, self).context(**kwargs)
        content['person'] = self.content
        return context
