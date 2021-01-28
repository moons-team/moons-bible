from users.models import *
from thebible.models import *
import re
# 언어식별 라이브러리
import langid



# 검색
def ReadSearch(search_version, keyword):
    version_list = BibleVersions.version_choice
    for i in version_list:
        if i[1] == search_version:
            version_num = i[0]
    
    # 키워드가 포함된 절
    all_verse = BibleVerses.objects.filter(verse__icontains=keyword, BibleChapter__BibleTitle__BibleVersion__version=0)

    return all_verse