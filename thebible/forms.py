from django import forms

# 성경 키워드 검색
class read_search_form(forms.Form):
    # keyword
    keyword = forms.CharField(label="", min_length=1, max_length=50, initial='' ,
                                error_messages={
                                    'required': u'검색어를 입력하십시오!',
                                    },
                                widget = forms.TextInput(attrs={
                                    # 'placeholder': '',
                                    'class': 'search_input',
                                })
                            )