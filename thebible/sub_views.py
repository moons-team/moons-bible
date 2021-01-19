from users.models import *
from thebible.models import *
import re

# 검색 api
def ReadSearch(search_version, keyword):
    version_list = BibleVersions.version_choice
    for i in version_list:
        if i[1] == search_version:
            version_num = i[0]
    
    result_list = [] # 검색결과 리스트
    version = BibleVersions.objects.get(version=version_num) # 해당 버전 가져오기
    all_title = BibleTitles.objects.filter(BibleVersion_id=version.id) # 해당버전 모든 제목 가져오기
    for title in all_title:
        all_chapter = BibleChapters.objects.filter(BibleTitle_id=title.id) # 해당 제목 모든 장 가져오기
        for chapter in all_chapter:
            all_verse = BibleVerses.objects.filter(BibleChapter_id=chapter.id)
            for verse in all_verse:
                search_verse = verse.verse
                re_search_verse = re.findall(r'{}'.format(keyword), search_verse)
                if re_search_verse == []:
                    pass
                else:
                    result_list.append(verse.id) 
    print(result_list)
    result = 1
    return result