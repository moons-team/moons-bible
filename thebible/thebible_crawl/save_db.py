# -------------장고 orm 사용 목적------------------
import os
import sys
import django
 
sys.path.append('/Users/moons-featuring/Desktop/mysite/mysite')	# 프로젝트의 절대경로
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 	# settings.py가 있는곳
django.setup()
# ----------------------------------------------


from run_crawl import start_crawling

from thebible.models import BibleVersions, BibleTitles, BibleChapters, BibleVerses

def save_to_db(version, language, version_name):
    all_bible_content = start_crawling(version, language, version_name)
    print(len(all_bible_content))
    count = 0
    for one_bible_content in all_bible_content:
        for bible_content in one_bible_content:
            count += 1
            language = bible_content['language']  # 성경언어
            version = bible_content['version_name']  # 성경버전
            title_type = bible_content['title_type']  # 제목타입
            title_num = bible_content['title_num']  # 제목넘버
            title = bible_content['title']  # 제목
            chapter_num = bible_content['chapter_num']  # 장
            verse_num = bible_content['verse_num']  # 절
            verse = bible_content['verse']  # 내용
            BibleVersions_table, ture_and_false = BibleVersions.objects.get_or_create(language=language, version=version)
            BibleTitles_table, ture_and_false = BibleTitles.objects.get_or_create(BibleVersion_id=BibleVersions_table.id, title_type=title_type, title=title, title_num=title_num)
            BibleChapters_table, ture_and_false = BibleChapters.objects.get_or_create(BibleTitle_id=BibleTitles_table.id, chapter_num=chapter_num)
            BibleVerses_table = BibleVerses.objects.create(BibleChapter_id=BibleChapters_table.id, verse_num=verse_num, verse=verse)
            BibleVerses_table.save()
    print(count)
    