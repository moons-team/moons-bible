from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
from django.urls import reverse

# 유저 관련
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import UserProfile

# 폼
from users.forms import login_form, signup_form

# 언어식별 라이브러리
import langid

# Create your views here.

# 로그인
class LoginView(View):
    def get(self, request):
        login_input = login_form()
        info = {
            "login_input": login_input,
            "error": '',
        }
        return render(request, 'login.html', info)

    def post(self, request):
        login_input = login_form()
        info = {
            "login_input": login_input,
            "error": '',
        }
        email = request.POST["email"]
        password = request.POST["password"]
        # 유저가 회원가입 되었는지 확인
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
        else:
            info['error'] = "가입되지 않았거나 비밀번호가 틀렸습니다!"
            return render(request, 'login.html', info)

        # 이전페이지 경로
        next_path = request.POST["next_path"]
        return redirect(next_path)

# 로그아웃
def logout_view(request):
    logout(request)
    # 이전페이지 경로
    next_path = request.GET["next_path"]
    return redirect(next_path)

# 회원가입
class SignupView(View):
    def get(self, request):
        signup_input = signup_form()
        info = {
            "signup_input": signup_input,
            "error": '',
        }
        return render(request, 'signup.html', info)

    def post(self, request):
        signup_input = signup_form()
        info = {
            "signup_input": signup_input,
            "error": '',
        }
        email = request.POST["email"]
        password = request.POST["password"]
        password_check = request.POST["password_check"]
        user = User.objects.filter(username=email).count()
        # 유저가 있다면?
        if user == 1:
            info['error'] = "이미 회원가입된 메일입니다!"
            return render(request, "signup.html", info)
        # 비밀번호가 일치하지 않다면?
        if password_check != password:
            info['error'] = "비밀번호가 일치하지 않습니다!"
            return render(request, "signup.html", info)

        name = request.POST["name"]
        user = User.objects.create_user(username=email, email=email, password=password)
        user.last_name = name
        user.save()
        UserProfile_db = UserProfile.objects.create(user_key_id=user.id, profile_img='img/user_profile_img/default.jpg', introduction="", affiliation="", language=langid.classify(name)[0])
        UserProfile_db.save()
        
        # 로그인
        user = authenticate(username=email, password=password)
        login(request, user)

        # 이전페이지 경로
        next_path = request.POST["next_path"]
        return redirect(next_path)