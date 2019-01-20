from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, SignUpView

urlpatterns = [
    url(r'home$', home, name="movieholic_home"),
    url(r'login$',
        LoginView.as_view(template_name="movieholic/login_form.html"),
        name="movieholic_login"),
    url(r'logout$',
        LogoutView.as_view(),
        name="movieholic_logout"),
    url(r'signup$', SignUpView.as_view(), name='movieholic_signup'),
]
