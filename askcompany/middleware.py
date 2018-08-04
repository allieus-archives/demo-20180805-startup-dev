import json
from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .encoders import JSONEncoder


class JsonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and request.body:
            content_type = request.META.get('CONTENT_TYPE', '')
            if 'application/json' in content_type:
                request.JSON = json.loads(request.body)

    def process_response(self, request, response):
        if isinstance(response, str):
            if response and response[0] in ('"', '[', '{'):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (set, dict, list, tuple, QuerySet, Model)):
            return JsonResponse(response, encoder=JSONEncoder, safe=False,
                                json_dumps_params={'ensure_ascii': True})
        else:
            return response
