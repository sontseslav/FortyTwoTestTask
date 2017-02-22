from apps.hello.models import MyHttpRequest


class ReqRespMiddleware(object):

    def process_request(self, request):
        self.method = request.META['REQUEST_METHOD']
        # path_info
        self.path = request.path_info
        self.server_protocol = request.META['SERVER_PROTOCOL']

    def process_response(self, request, response):
        self.status = response.status_code
        self.response_length = len(response.content)
        myresp = MyHttpRequest(method=self.method,
                               path=self.path,
                               server_protocol=self.server_protocol,
                               status=self.status,
                               response_length=self.response_length)
        myresp.save()
        return response
