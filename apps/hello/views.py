from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from apps.hello.models import Person, HttpRequest


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


class RequestsView(ListView):
    template_name = "hello/request_list.html"
    model = HttpRequest
    content = None

    def get(self, request, *args, **kwargs):
        # insane
        self.content = {
                "id": "101",
                "method": "GET",
                "path": "/",
                "server_protocol": "HTTP/1.1",
                "status": 200,
                "response_length": "12345",
                "date": "2017-02-19T00:00:00"
        }
        return super(RequestsView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super(RequestsView, self).get_context_data(**kwargs)
        # insane
        content['object_list'] = self.content
        return content
