from django.shortcuts import HttpResponse
from django.views.generic.base import View
from users.models import *
from thebible.models import *

# 유저가 좋아하는 성구 api
class like_verse_api(View):
    def post(self, request, **kwargs):
        is_active = request.POST.get('is_active')
        verseid = request.POST.get('verseid')
        # 유저
        current_user = request.user
        if current_user.is_authenticated:
            # 성구
            BibleVerse = BibleVerses.objects.get(id=verseid)
            if is_active == "false":
                # 저장
                UserLikeVerse = UserLikeVerses.objects.create(user_id=current_user.id, verse_id=verseid)
                UserLikeVerse.save()
                # 해당 버전 현재 북마크 수 + 1
                BibleVerse = BibleVerses.objects.get(id=verseid)
                now_like_count = BibleVerse.now_like_count
                BibleVerse.now_like_count = now_like_count + 1
                # 해당 버전 누적 북마크수 + 1
                all_like_count = BibleVerse.all_like_count
                BibleVerse.all_like_count = all_like_count + 1
                BibleVerse.save()
                return HttpResponse(1) # 저장 되었습니다
            else:
                # 제거
                UserLikeVerse = UserLikeVerses.objects.filter(user_id=current_user.id, verse_id=verseid).first()
                UserLikeVerse.delete()
                # 해당 버전 현재 북마크 수 -1
                BibleVerse = BibleVerses.objects.get(id=verseid)
                now_like_count = BibleVerse.now_like_count
                BibleVerse.now_like_count = now_like_count - 1
                BibleVerse.save()

                return HttpResponse(0) # 제거 되었습니다
        else: # 로그인 안되어 있을 경우
            return HttpResponse(2)