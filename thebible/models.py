from django.db import models

# Create your models here.

# 성경 버전 테이블
class BibleVersions(models.Model):
    language_choice=(
        (0,"korea"),
        (1,"china"),
        )
    version_choice=(
        (0,"개역개정"),
        (1,"개역한글"),
        (2,"공동번역"),
        (3,"새번역"),
        (4,"현대인"),
        (5,"简体"),
        (6,"繁体"),
        )
    # 성경 버전
    version = models.IntegerField(choices=version_choice, default=0, verbose_name="성경버전")
    # 성경 언어
    language = models.IntegerField(choices=language_choice, default=0, verbose_name="성경언어")
    # 업데이트 시간
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="업데이트 시간")
    
    class Meta:
        # 타이틀명 바꾸기
        verbose_name_plural = '성경 버전'
        verbose_name = '성경 버전'
        # 배열
        ordering = ['id']
        # 테이블명 바꾸기
        db_table = 'BibleVersions'

    # def __str__(self):
    #     return self.version

# 성경 제목 테이블
class BibleTitles(models.Model):
    title_type_choice=(
        (0,"구약"), (1,"신약"), (2,"旧约"), (3,"新约"), (4,"舊約"), (5,"新約"),
    )
    # 제목
    title_num = models.IntegerField(blank=True, null=True, verbose_name="제목넘버")
    # 제목
    title = models.CharField(max_length=30, blank=True, null=True, verbose_name="제목")
    # 타입
    title_type = models.IntegerField(choices=title_type_choice, default=0, verbose_name="타입")
    # 업데이트 시간
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="업데이트 시간")

    # 포링키
    BibleVersion = models.ForeignKey(BibleVersions, on_delete=models.CASCADE)

    class Meta:
        # 타이틀명 바꾸기
        verbose_name_plural = '성경 제목'
        verbose_name = '성경 제목'
        # 배열
        ordering = ['id']
        # 테이블명 바꾸기
        db_table = 'BibleTitles'

    def __str__(self):
        return self.title

# 성경 장 테이블
class BibleChapters(models.Model):
    # 성경 장
    chapter_num = models.IntegerField(blank=True, null=True, verbose_name="장")
    # 업데이트 시간
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="업데이트 시간")

    # 포링키
    BibleTitle = models.ForeignKey(BibleTitles, on_delete=models.CASCADE)

    class Meta:
        # 타이틀명 바꾸기
        verbose_name_plural = '성경 장'
        verbose_name = '성경 장'
        # 배열
        ordering = ['id']
        # 테이블명 바꾸기
        db_table = 'BibleChapters'

    # def __str__(self):
    #     return self.chapter_num
        
# 성경 절 테이블
class BibleVerses(models.Model):
    # 성경 절 넘버
    verse_num = models.IntegerField(blank=True, null=True, verbose_name="절")
    # 성경 절 내용
    verse = models.TextField(blank=True, null=True, verbose_name="내용" ,db_index=True)
    # 누적 복사 수
    all_copy_count = models.IntegerField(default=0, verbose_name="누적 복사 회수")
    # 현재 좋아요 수
    now_like_count = models.IntegerField(default=0, verbose_name="현재 좋아요 회수")
    # 누적 좋아요 수
    all_like_count = models.IntegerField(default=0, verbose_name="누적 좋아요 회수")
    # 업데이트 시간
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="업데이트 시간")

    # 포링키
    BibleChapter = models.ForeignKey(BibleChapters, on_delete=models.CASCADE)

    class Meta:
        # 타이틀명 바꾸기
        verbose_name_plural = '성경 절'
        verbose_name = '성경 절'
        # 배열
        ordering = ['id']
        # 테이블명 바꾸기
        db_table = 'BibleVerses'

    def __str__(self):
        return self.verse