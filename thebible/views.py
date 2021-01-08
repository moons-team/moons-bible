from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from thebible.forms import read_search_form

from thebible.models import *

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
        read_search_input = read_search_form()
        para_list = [
            ['?vs_one=', ''],
            ['&vs_two=', ''],
            ['&title=', ''],
            ['&chapter=', ''],
        ]

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

        context = {
            # 버전1
            "version_one": version_one.get_version_display(),
            # 버전2
            "version_two": version_two.get_version_display(),
            # 버전 리스트
            "version_list": version_list,
            # 제목 리스트
            "title_list": title_list,
            # 장 리스트
            "chapter_list": chapter_list,
            # 파라메터 리스트
            "para_list": para_list,
            # 버전별 제목
            "version_one_title": version_one_title,
            "version_two_title": version_two_title,
            # 버전별 내용
            "version_one_title_chapter_content": version_one_title_chapter_content,
            "version_two_title_chapter_content": version_two_title_chapter_content,
            # 버전별 언어 장
            "version_one_language_title": version_one_language_title,
            "version_two_language_title": version_two_language_title,
            # 검색
            "read_search_input": read_search_input,
        }
        return context
    
    def post(self, request):
        return render(request, "login.html")