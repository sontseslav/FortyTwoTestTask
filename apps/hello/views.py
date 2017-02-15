from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)

    def context(self, **kwargs):
        context = super(IndexView, self).context(**kwargs)
        return context
