from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login', kwargs={
        'form_class': LoginForm,
    }),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={
        'next_page': settings.LOGIN_URL,  # LogoutView CBV에서는 현재 처리되고 있지 않음.
    }),
    url(r'^profile/$', views.profile, name='profile'),
]

