import json
from functools import wraps
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

def before(view_fn):
    @wraps(view_fn)
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            request.JSON = json.loads(request.body.decode('utf8'))
        else:
            request.JSON = {}

        user_key = kwargs.get('user_key')
        user_key = request.JSON.get('user_key', user_key)
        user_key = kwargs.get('user_key', user_key)

        if user_key:
            username = 'kakao-' + user_key
            try:
                request.user = User.objects.get(username=username)
            except User.DoesNotExist:
                request.user = User.objects.create_user(username=username)

        request.user_key = user_key

        return JsonResponse(view_fn(request, *args, **kwargs) or {})
    return wrap

