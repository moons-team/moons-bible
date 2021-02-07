from django import template

register = template.Library()

# 리스트 길이계산
@register.filter(name='lenth')
def lenth(this_list):
    return len(this_list)