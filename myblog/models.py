from django.db import models

# Create your models here.

# 블로그 글 테이블
# class blog_content(models.Model):
#     # 제목
#     title = models.CharField(max_length=130, blank=True, null=True, verbose_name="제목")
#     class Meta:
#         # 타이틀명 바꾸기
#         verbose_name_plural = '블로그'
#         verbose_name = '블로그'
#         # 배열
#         ordering = ['id']
#         # 테이블명 바꾸기
#         db_table = 'blog_content'

#     # 내용을 키워드로 표시
#     def __str__(self):
#         return self.title
