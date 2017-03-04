from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from apps.hello.models import Person, MyHttpRequest


class IndexView(TemplateView):
    template_name = 'hello/index.html'
    model = Person

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['person'] = Person.objects.first()
        return context


class RequestsView(ListView):
    template_name = "hello/request_list.html"
    model = MyHttpRequest
    content = None

    def get(self, request, *args, **kwargs):
        # Desc order - first 10 nonviewed requests
        self.content = MyHttpRequest.objects.filter(
            viewed=False
            ).order_by('date')[:10]
        return super(RequestsView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super(RequestsView, self).get_context_data(**kwargs)
        content['object_list'] = self.content
        # matching all requests as viewed
        for request in self.content:
            request.viewed = True
            request.save()
        return content

    def post(self, request, *args, **kwargs):
        self.content = MyHttpRequest.objects.filter(
            viewed=False
            ).order_by('date')[:10]
        # matching all requests as viewed
        for request in self.content:
            request.viewed = True
            request.save()
        return render_to_response(
            'hello/post_response.html',
            {'object_list': self.content},
            content_type="text/html"
            )
