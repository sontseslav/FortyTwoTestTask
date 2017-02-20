from models import HttpRequest


class ReqRespMiddleware(object):

    def process_response(self, request, response):
        data = HttpRequest(method=request.META['REQUEST_METHOD'],
                           path=request.path,
                           server_protocol=request.META['SERVER_PROTOCOL'],
                           status=response.status_code,
                           response_length=len(response.content))
        data.save()
        return response
