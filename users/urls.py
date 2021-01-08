from django.urls import path
from users import views

app_name = "user"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.SignupView.as_view(), name="signup"),
]
