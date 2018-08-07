from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from . import actions


def index(request):
    return render(request, 'dialogflow/index.html', {
        'WEB_DEMO_URL': settings.DIALOGFLOW['WEB_DEMO_URL'],
    })


@require_POST
@csrf_exempt
def fulfillment(request):
    # intent_name = request.JSON['result']['metadata']['intentName']
    action_name = request.JSON['result']['action'].replace('-', '_')
    params = request.JSON['result']['parameters']

    action = getattr(actions, action_name, None)

    if callable(action):
        response = action(**params)
    else:
        response = {
            'speech': '제가 처리할 수 없는 부분입니다.',
        }

    return response

