from django.db import models
from django.contrib.auth.models import User as User_db
from thebible.models import BibleVerses

# Create your models here.
class UserProfile(models.Model):
    # 프로필 사진
    profile_img = models.ImageField(upload_to='img/user_profile_img/', default='img/user_profile_img/default.jpg', verbose_name="프로필 사진")
    # 소개
    introduction = models.TextField(blank=True, null=True, verbose_name="소개")
    # 소속 교단
    affiliation = models.CharField(max_length=30, blank=True, null=True, verbose_name="소속교단")
    # 언어
    language = models.CharField(max_length=30, blank=True, null=True, verbose_name="언어")
    # 생성 시간
    create_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="생성 시간")

    # 포링키
    user_key = models.ForeignKey(User_db, on_delete=models.CASCADE)
    
    # 풀네임
    full_name = "이후 수정"

    class Meta:
        # 타이틀명 바꾸기
        verbose_name_plural = '유저 프로필'
        verbose_name = '유저 프로필'
        # 배열
        ordering = ['id']
        # 테이블명 바꾸기
        db_table = 'UserProfile'

    def __str__(self):
        return self.full_name

# 유저가 좋아하는 성구
class UserLikeVerses(models.Model):
    # 유저
    user = models.ForeignKey(User_db, on_delete=models.DO_NOTHING)
    # 성구
    verse = models.ForeignKey(BibleVerses, on_delete=models.DO_NOTHING)
    # 저장시간
    save_time = models.DateTimeField(auto_now_add=True, verbose_name="저장 시간")

    def __unicode__(self):
        return "유저%s가 좋아하는 성구는 %s" % (self.user_key, self.verse_key)
