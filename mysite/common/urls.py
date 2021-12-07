from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "common"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

# https://docs.djangoproject.com/en/3.2/topics/auth/default/#django.contrib.auth.views.LoginView
##장고가 기본적으로 제공하는 auth view 에  form, view 기능들이 있음.
