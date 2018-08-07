from dialogflow.utils import query_speech
from requests.exceptions import HTTPError
from .decorators import before


@before
def on_init(request):
    return {
        'type': 'buttons',
        'buttons': ['안녕하세요. :)'],
    }


@before
def on_message(request):
    message_type = request.JSON['type']        # text, photo, audio(m4a), video(mp4)
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL

    if message_type == 'text':
        session_id = request.user.username
        try:
            response = query_speech(session_id, content, lang=None, timezone=None)
        except HTTPError:
            speech = '에러: 처리 중에 오류가 발생했습니다. 잠시 후 다시 시도해주세요.'
        else:
            from pprint import pprint
            pprint(response)
            speech = response['result']['fulfillment']['speech']
    else:
        speech = '{}타입 메세지는 지원하지 않습니다.'.format(message_type)

    return {
        'message': {
            'text': speech,
        }
    }


@before
def on_added(request):
    pass


@before
def on_block(request, user_key):
    pass


@before
def on_leave(request, user_key):
    pass

