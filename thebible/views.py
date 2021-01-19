from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from thebible.forms import read_search_form

from thebible.models import *
from users.models import *
from thebible.sub_views import *

# Create your views here.
# 성경 홈 페이지
class thebible_home(View):
    def get(self, request):
        context = {
            "a": "da",
        }
        return render(request, 'home/thebible_home.html', context=context)

# 성경읽기 페이지
class thebible_read(TemplateView):

    template_name = 'read/thebible_read.html'

    def get_context_data(self, **kwargs):
        context = {}

        read_search_input = read_search_form()
        context["read_search_input"] = read_search_input # 검색 폼
        para_list = [['?vs_one=', ''],['&vs_two=', ''],['&title=', ''],['&chapter=', '']]
        
        # 버전 1
        vs_one_filter = self.request.GET.get('vs_one', 1)
        para_list[0][1] = vs_one_filter
        # 버전 2
        vs_two_filter = self.request.GET.get('vs_two', 5)
        para_list[1][1] = vs_two_filter
        # 제목
        title_filter = self.request.GET.get('title', 1)
        para_list[2][1] = title_filter
        # 장
        chapter_filter = self.request.GET.get('chapter', 1)
        para_list[3][1] = chapter_filter

        # 버전 1
        version_one = BibleVersions.objects.get(version=para_list[0][1])
        # 버전 1 제목
        version_one_title = version_one.bibletitles_set.all().get(title_num=para_list[2][1])
        # 버전 1 제목 장
        version_one_title_chapter = version_one_title.biblechapters_set.get(chapter_num=para_list[3][1])
        # 버전 1 제목 장 내용
        version_one_title_chapter_content = version_one_title_chapter.bibleverses_set.all()
        # 버전 2
        version_two = BibleVersions.objects.get(version=para_list[1][1])
        # 버전 2 제목
        version_two_title = version_two.bibletitles_set.get(title_num=para_list[2][1])
        # 버전 2 제목 장
        version_two_title_chapter = version_two_title.biblechapters_set.get(chapter_num=para_list[3][1])
        # 버전 2 제목 장 내용
        version_two_title_chapter_content = version_two_title_chapter.bibleverses_set.all()

        # 버전 리스트
        version_list = BibleVersions.version_choice
        # 제목 리스트
        title_list = version_one.bibletitles_set.all()
        # 장 리스트
        chapter_list = version_one_title.biblechapters_set.all()

        version_one_language_title = '장'
        version_two_language_title = '장'
        if para_list[0][1] == '5' or para_list[0][1] == '6':
            version_one_language_title = '章'
        if para_list[1][1] == '5' or para_list[1][1] == '6':
            version_two_language_title = '章'
        
        context["like_verse_id_list"] = []
        # 유저 좋아요
        current_user = self.request.user
        if current_user.is_authenticated:
            UserLikeVerse_list = UserLikeVerses.objects.filter(user_id=current_user.id)
            like_verse_id_list = []
            if UserLikeVerse_list:
                for i in UserLikeVerse_list:
                    like_verse_id_list.append(i.verse.id)
            context["like_verse_id_list"] = like_verse_id_list
        
        context["version_one"] = version_one.get_version_display() # 버전1
        context["version_two"] = version_two.get_version_display() # 버전2
        context["version_list"] = version_list # 필터 버전 리스트
        context["title_list"] = title_list # 필터 제목 리스트
        context["chapter_list"] = chapter_list # 필터 장 리스트
        context["para_list"] = para_list # 필터 파라메터 리스트
        context["version_one_title"] = version_one_title # 버전1의 제목
        context["version_two_title"] = version_two_title # 버전2의 제목
        context["version_one_title_chapter_content"] = version_one_title_chapter_content # 버전1의 내용
        context["version_two_title_chapter_content"] = version_two_title_chapter_content # 버전2의 내용
        context["version_one_language_title"] = version_one_language_title # 버전1의 장
        context["version_two_language_title"] = version_two_language_title # 버전2의 장
        
        return context

# 검색 뷰
class SearchReadView(thebible_read):
    template_name = 'read/thebible_read.html'
    def get_context_data(self, **kwargs):
        context = super(SearchReadView, self).get_context_data(**kwargs)

        keyword = self.request.GET.get("keyword", "하나님") # 검색키워드
        search_version = self.request.GET.get("search_version", "개역한글") # 검색 버전
        # 검색 펑션 호출
        search_result = ReadSearch(search_version, keyword)
        # 검색 결과
        context['search_result'] = search_result
        return context
    