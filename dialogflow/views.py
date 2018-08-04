from pprint import pprint
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from . import actions
# from .models import Pizza


def index(request):
    return render(request, 'dialogflow/index.html', {
        'WEB_DEMO_URL': settings.DIALOGFLOW['WEB_DEMO_URL'],
    })


@csrf_exempt
@require_POST
def fulfillment(request):
    # request.JSON: intent에서 먼저 처리한 내역
    action_name = request.JSON['result']['action'].replace('-', '_')
    params = request.JSON['result']['parameters']

    action = getattr(actions, action_name, None)
    if callable(action):
        speech = action(**params)
    else:
        speech = '제가 처리할 수 없는 부분입니다.'

    return {
        'speech': speech,
    }

