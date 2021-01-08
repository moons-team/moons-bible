from get_source import get_bible_source
from parser import analysis_bible_source
from bar import ProgressBar

# 크롤링 시작
def start_crawling(version, language, version_name):
    all_bible_content = []
    bar = ProgressBar(total = 100)
    # 성경 66권 크롤링
    for title_num in range(67): #67
        if title_num == 0:
            continue
        chapter_num = 0
        # 장수 크롤링
        while True:
            chapter_num += 1
            page_source = get_bible_source(version, title_num, chapter_num)
            one_chapter_content = analysis_bible_source(page_source, version, title_num, language, version_name)
            if one_chapter_content: #  and chapter_num <= 1
                all_bible_content.append(one_chapter_content)
                bar.move()
                bar.log(name=version_name)
            else:
                break
    return all_bible_content