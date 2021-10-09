from django.utils.deprecation import MiddlewareMixin


class MyCors(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = "content-type, authorization"
        return response

    # 屏蔽csrf检查
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
