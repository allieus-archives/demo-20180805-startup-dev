import pandas as pd
import requests
from bs4 import BeautifulSoup


USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')


def 블로그_검색(query):
    url = 'https://search.naver.com/search.naver'

    params = {
        'where': 'post',
        'query': query,
    }

    headers = {
        'User-Agent': USER_AGENT,
    }

    res = requests.get(url, params=params, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    post_list = []

    for tag in soup.select('.sh_blog_top'):
        title_tag = tag.select_one('.sh_blog_title')

        url = title_tag['href']
        title = title_tag.text
        desc = tag.select_one('.sh_blog_passage').text
        thumb_url = tag.select_one('img')['src']
        when = tag.select_one('.txt_inline').text

        post_list.append({
            'title': title,
            'desc': desc,
            'thumb_url': thumb_url,
            'when': when,
            'url': url,
        })

    return post_list


def 상한가_크롤링():
    '''
    네이버 금융 - 상한가 페이지 크롤링

    https://finance.naver.com/sise/sise_upper.nhn
    '''

    url = 'https://finance.naver.com/sise/sise_upper.nhn'

    # 파이썬에서 동작하는 브라우저인 requests를 통해,
    # 지정 URL의 서버로 요청을 보내어 응답을 받습니다.
    res = requests.get(url)

    # 받은 응답의 문자열을 html 변수에 저장합니다.
    html = res.text

    # 파싱을 위해, 아름다운스프 객체를 생성합니다.
    soup = BeautifulSoup(html, 'html.parser')

    df_list = []
    for tag in soup.select('.box_type_l'):
        category = tag.select_one('.top_tlt').text
        row_list = []
        for tr_tag in tag.select('table tr'):
            col_text_list = [
                tag.text.strip()
                for tag in tr_tag.select('th, td')
                if tag.text.strip()]
            if col_text_list:
                row_list.append(col_text_list)
          
        df = pd.DataFrame(row_list[1:], columns=row_list[0]).set_index('N')
        df['분류'] = category
        df_list.append(df)
        
    df = pd.concat(df_list)

    columns = ['분류', '종목명', '현재가', '등락률', '거래량']
    return df[columns].to_string()


def 테마별_시세_크롤링():
    url = 'https://finance.naver.com/sise/theme.nhn'

    df = pd.read_html(url, encoding='cp949')[0].iloc[3:]
    df.columns = [
        '테마명', '전일대비', '최근3일등락률(평균)',
        '전일대비등락현황 (상승)',
        '전일대비등락현황 (보합)',
        '전일대비등락현황 (하락)',
        '주도주1', '주도주2']
    df = df.set_index('테마명')

    columns = ['전일대비', '최근3일등락률(평균)', '주도주1', '주도주2']
    return df[columns].iloc[:3].to_string()

