from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from apps.hello.models import Person, MyHttpRequest


class IndexView(TemplateView):
    template_name = 'hello/index.html'
    model = Person
    content = None

    def get(self, request, *args, **kwargs):
        self.content = Person.objects.first()
        return super(IndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super(IndexView, self).get_context_data(**kwargs)
        content['person'] = self.content
        return content


class RequestsView(ListView):
    template_name = "hello/request_list.html"
    model = MyHttpRequest
    content = None

    def get(self, request, *args, **kwargs):
        # Desc order - first 10 nonviewed requests
        self.content = MyHttpRequest.objects.filter(viewed=False)[:10]
        return super(RequestsView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super(RequestsView, self).get_context_data(**kwargs)
        content['object_list'] = self.content
        # matching all requests as viewed
        for request in self.content:
            request.viewed = True
            request.save()
        return content
