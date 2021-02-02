from users.models import *
from thebible.models import *
from django.db.models import Q

import langid # 언어식별 라이브러리


# 버전 제목 장 검색 횟수 +1
def increase_search_count(version_num, title_num, chapter_num):
    version_db = BibleVersions.objects.get(version=version_num)
    version_db.search_count += 1
    version_db.save()
    title_db = version_db.bibletitles_set.get(title_num=title_num)
    title_db.search_count += 1
    title_db.save()
    chapter_db = title_db.biblechapters_set.get(chapter_num=chapter_num)
    chapter_db.search_count += 1
    chapter_db.save()


# 키워드 검색 횟수 +1 저장도 여기서 함
def keyword_search_count(keyword):
    keyword_db, is_save = KeywordsInfo.objects.get_or_create(keyword=keyword)
    keyword_db.search_count += 1
    keyword_db.save()


# 해당 버전 검색
def ReadSearch(search_version, keyword):
    version_list = BibleVersions.version_choice
    for i in version_list:
        if i[1] == search_version:
            version_num = i[0]
            break
    
    # 키워드가 포함된 절
    all_verse = BibleVerses.objects.filter(Q(verse__icontains=keyword)|Q(BibleChapter__BibleTitle__title__icontains=keyword), BibleChapter__BibleTitle__BibleVersion__version=version_num).values('BibleChapter__BibleTitle__title', "BibleChapter__chapter_num", "verse_num", "verse")
    result_count = all_verse.count()
    version_db = BibleVersions.objects.get(version=version_num)
    version_db.search_count += 1
    version_db.save()
    keyword_search_count(keyword)

    result = {}
    for i in all_verse:
        if i['BibleChapter__BibleTitle__title'] not in result:
            result[i['BibleChapter__BibleTitle__title']] = {i['BibleChapter__chapter_num']: [{'verse_num': i['verse_num'], 'verse': i['verse']}]}
        else:
            if i['BibleChapter__chapter_num'] not in result[i['BibleChapter__BibleTitle__title']]:
                result[i['BibleChapter__BibleTitle__title']][i['BibleChapter__chapter_num']] = [{'verse_num': i['verse_num'], 'verse': i['verse']}]
            else:
                result[i['BibleChapter__BibleTitle__title']][i['BibleChapter__chapter_num']].append({'verse_num': i['verse_num'], 'verse': i['verse']})

    return result, result_count