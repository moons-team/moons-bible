from django import forms

# 로그인 폼
class login_form(forms.Form):
    # 이메일
    email = forms.EmailField(label="", min_length=3, max_length=30, initial='',
                                error_messages={
                                    'required': u'이메일을 입력하십시오!',
                                    },
                                widget = forms.EmailInput(attrs={
                                    # 'placeholder': '이메일을 입력하십시오!',
                                    'id': 'user',
                                })
                            )
    # 비밀번호
    password = forms.CharField(label="", min_length=6, max_length=20, initial='' ,
                                error_messages={
                                    'required': u'비밀번호를 입력하십시오!',
                                    'min_length': u'6자 이상 입력하십시오!',
                                    'max_length': u'20자 이하로 입력하십시오!',
                                    },
                                widget = forms.PasswordInput(attrs={
                                    # 'placeholder': '6~20글의 비밀번호를 입력하십시오',
                                    'id': 'pswd',
                                })
                            )

# 회원가입 폼
class signup_form(forms.Form):
    # 이름
    name = forms.CharField(label="", min_length=1, max_length=20, initial='',
                                error_messages={
                                    'required': u'이름을 입력하십시오!',
                                    },
                                widget = forms.TextInput(attrs={
                                    # 'placeholder': '이름을 입력하십시오!',
                                })
                        )
    # 이메일
    email = forms.EmailField(label="", min_length=3, max_length=30, initial='',
                                error_messages={
                                    'required': u'이메일을 입력하십시오!',
                                    },
                                widget = forms.EmailInput(attrs={
                                    # 'placeholder': '이메일을 입력하십시오!',
                                })
                            )
    # 비밀번호
    password = forms.CharField(label="", min_length=6, max_length=20, initial='' ,
                                error_messages={
                                    'required': u'비밀번호를 입력하십시오!',
                                    'min_length': u'6자 이상 입력하십시오!',
                                    'max_length': u'20자 이하로 입력하십시오!',
                                    },
                                widget = forms.PasswordInput(attrs={
                                    # 'placeholder': '6~20글의 비밀번호를 입력하십시오',
                                })
                            )
    # 비밀번호 확인
    password_check = forms.CharField(label="", min_length=6, max_length=20, initial='' ,
                                error_messages={
                                    'required': u'비밀번호를 입력하십시오!',
                                    'min_length': u'6자 이상 입력하십시오!',
                                    'max_length': u'20자 이하로 입력하십시오!',
                                    },
                                widget = forms.PasswordInput(attrs={
                                    # 'placeholder': '비밀번호 확인',
                                })
                            )
