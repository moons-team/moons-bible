import requests
import time

# html 소스 가져오기
def get_bible_source(version, title_num, chapter_num):
    url = "http://www.holybible.or.kr/{}/cgi/bibleftxt.php?VR={}&VL={}&CN={}".format(version, version[2:], title_num, chapter_num)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'http://www.holybible.or.kr/',
        'Upgrade-Insecure-Requests': '1',
        }
    # for i in range(5):
    #     try:
    page_source = requests.get(url, headers=headers, timeout=(3,7))
    new_page_source = page_source.text.encode(page_source.encoding).decode(page_source.apparent_encoding, 'ignore')
        #     break
        # except:
        #     new_page_source = ''
        #     print("오류 발생! 3초후 다시 시도합니다...")
        #     time.sleep(3)
        #     print("재 실행중...({}회쨰)".format(i+1))

    return new_page_source