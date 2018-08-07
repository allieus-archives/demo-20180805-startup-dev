import random
from django.template.loader import render_to_string
from .naver import 블로그_검색, 상한가_크롤링, 테마별_시세_크롤링


def search(search_engine, keyword):
    if search_engine == '네이버 블로그':
        post_list = 블로그_검색(keyword)
        speech = render_to_string('dialogflow/naver_blog_search_result.txt', {
            'post_list': post_list[:3],
        })
    else:
        speech = '{}는 지원하지 않습니다.'.format(search_engine)

    return {'speech': speech}


def stock_search(stock_search_term):
    if stock_search_term == '상한가 종목':
        speech = 상한가_크롤링()

    elif stock_search_term == '테마별 시세':
        speech = 테마별_시세_크롤링()

    else:
        speech = '{}는 지원하지 않습니다.'.format(stock_search_term)

    return {'speech': speech}

