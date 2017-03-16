from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from apps.hello.models import Person, MyHttpRequest


class IndexView(TemplateView):
    template_name = 'hello/index.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['person'] = Person.objects.first()
        return context


class RequestsView(ListView):
    template_name = "hello/request_list.html"
    model = MyHttpRequest

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        content = MyHttpRequest.objects.all().order_by(
            'date')[:10]
        context['object_list'] = content
        # matching all requests as viewed
        for request in content:
            request.viewed = True
            request.save()
        return context

    def post(self, request, *args, **kwargs):
        content = MyHttpRequest.objects.filter(
            viewed=False
            ).order_by('date')[:10]
        # matching all requests as viewed
        for request in content:
            request.viewed = True
            request.save()
        return render_to_response(
            'hello/post_response.html',
            {'object_list': content},
            content_type="text/html"
            )
