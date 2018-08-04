from dialogflow.utils import query_speech
from .decorators import before


@before
def on_init(request):
    return {
        'type': 'buttons',
        'buttons': ['안녕'],
    }


@before
def on_message(request):
    type = request.JSON['type']        # text, photo, audio(m4a), video(mp4)
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL

    if type == 'text':
        session_id = request.user.username
        response = query_speech(session_id, content)
    else:
        response = '처리할 수 없는 메세지를 주셨습니다.'

    return {
        'message': {
            'text': response,
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

