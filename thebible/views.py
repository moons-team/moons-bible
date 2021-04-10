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

# 상단 메뉴 바
class TopMenuDefault(TemplateView):
    def get_context_data(self, **kwargs):
        context = {}
        para_list = {}

        para_list['vs_one'] = int(self.request.GET.get('vs_one', 1))  # 버전 1
        para_list['vs_two'] = int(self.request.GET.get('vs_two', 5)) # 버전 2
        para_list['title'] = int(self.request.GET.get('title', 1)) # 제목
        para_list['chapter'] = int(self.request.GET.get('chapter', 1)) # 장
        context["para_list"] = para_list # 파라메터 리스트

        read_search_input = read_search_form()
        context["read_search_input"] = read_search_input # 검색 폼

        version_list = BibleVersions.version_choice
        context["version_list"] = version_list # 필터 버전 리스트
        title_list = BibleTitles.objects.filter(BibleVersion__version=para_list['vs_one']).order_by("title_num")
        context["title_list"] = title_list # 필터 제목 리스트
        chapter_list = BibleChapters.objects.filter(BibleTitle__BibleVersion__version=para_list['vs_one'], BibleTitle__title_num=para_list['title'])
        context["chapter_list"] = chapter_list # 필터 장 리스트

        context["version_one"] = version_list[para_list['vs_one']][1] # 버전1 이름
        context["version_two"] = version_list[para_list['vs_two']][1]# 버전2 이름

        context["version_one_title"] = BibleTitles.objects.get(title_num=para_list['title'], BibleVersion__version=para_list['vs_one']) # 버전1의 제목
        context["version_two_title"] = BibleTitles.objects.get(title_num=para_list['title'], BibleVersion__version=para_list['vs_two']) # 버전2의 제목

        context['now_version'] = "개역한글" # 현재 검색 버전
        context["search_version_language_subchapter"] = "장" # 검색된 버전 언어로 인한 ?장 혹은 ?章

        return context

# 성경읽기 페이지
class thebible_read(TopMenuDefault):

    template_name = 'read/thebible_read.html'

    def get_context_data(self, **kwargs):
        context = super(thebible_read, self).get_context_data(**kwargs)

        increase_search_count(context['para_list']['vs_one'], context['para_list']['title'], context['para_list']['chapter']) # 검색횟수 추가
        increase_search_count(context['para_list']['vs_two'], context['para_list']['title'], context['para_list']['chapter']) # 검색횟수 추가

        version_one_content = BibleVerses.objects.filter(BibleChapter__BibleTitle__BibleVersion__version=context['para_list']['vs_one'], BibleChapter__BibleTitle__title_num=context['para_list']['title'], BibleChapter__chapter_num=context['para_list']['chapter'])
        version_two_content = BibleVerses.objects.filter(BibleChapter__BibleTitle__BibleVersion__version=context['para_list']['vs_two'], BibleChapter__BibleTitle__title_num=context['para_list']['title'], BibleChapter__chapter_num=context['para_list']['chapter'])
        context["version_one_content"] = version_one_content # 버전1의 내용
        context["version_two_content"] = version_two_content # 버전2의 내용

        context["version_one_language_title"] = chapter_subname_language(context["version_one"]) # 버전1의 ?장 혹은 ?章
        context["version_two_language_title"] = chapter_subname_language(context["version_two"]) # 버전2의 ?장 혹은 ?章
        
        # 유저 좋아요
        current_user = self.request.user
        if current_user.is_authenticated:
            UserLikeVerse_list = UserLikeVerses.objects.filter(user_id=current_user.id)
            like_verse_id_list = []
            if UserLikeVerse_list:
                for i in UserLikeVerse_list:
                    like_verse_id_list.append(i.verse.id)
            context["like_verse_id_list"] = like_verse_id_list
        
        return context

    def post(self, request, **kwargs):
        context = super(thebible_read, self).get_context_data(**kwargs)

        keyword = self.request.POST.get("keyword", "하나님") # 검색키워드
        search_version = self.request.POST.get("search_version", "개역한글") # 검색 버전

        # 검색 펑션 호출
        search_result, result_count = ReadSearch(search_version, keyword)
        # 검색 결과
        context['search_result'] = search_result
        context['result_count'] = result_count

        context['now_version'] = search_version # 현재 검색 버전
        context["search_version_language_subchapter"] = chapter_subname_language(search_version) # 검색된 버전 언어 분별

        return render(request, 'read/thebible_read_search_result.html',context=context)

# 검색 뷰
class SearchReadView(TopMenuDefault):

    template_name = 'search/search_main.html'

    def get_context_data(self, **kwargs):
        context = super(SearchReadView, self).get_context_data(**kwargs)

        return context
    

import random

def test(request):
    context = {}

    bible = BibleVerses.objects.filter(userlikeverses__user_id=6, BibleChapter__BibleTitle__BibleVersion__version='1', BibleChapter__BibleTitle__title='잠언', BibleChapter__chapter_num__gte=9).values('BibleChapter__BibleTitle__title', 'BibleChapter__chapter_num', 'verse_num', 'verse')
    new_bible = list()
    for i in bible:
        new = {
            'title': f"{i['BibleChapter__BibleTitle__title']} {i['BibleChapter__chapter_num']}:{i['verse_num']}",
            'text': i['verse'],
        }
        new_bible.append(new)

    random.shuffle(new_bible)
    context['test'] = new_bible
    return render(request, 'test.html', context=context)