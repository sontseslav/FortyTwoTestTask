from django.views.generic.base import TemplateView
from apps.hello.models import Person


class IndexView(TemplateView):
    template_name = 'hello/index.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['person'] = Person.objects.first()
        return context
