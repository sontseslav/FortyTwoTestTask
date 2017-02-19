from django.views.generic.base import TemplateView
from apps.hello.models import Person


class IndexView(TemplateView):
    template_name = 'hello/index.html'
    model = Person
    content = None

    def get(self, request, *args, **kwargs):
        self.content = Person.objects.get(pk=1)
        return super(IndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super(IndexView, self).get_context_data(**kwargs)
        content['person'] = self.content
        return content


class RequestsView(TemplateView):
    template_name = "hello/request_list.html"
