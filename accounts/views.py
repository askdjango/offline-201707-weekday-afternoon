from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


def login(request):
    provider_list = []

    for provider in get_providers():
        try:
            # social_app속성은 provider에는 없는 속성입니다. 그래서 다음과 같이 커스텀 속성을 정의해봤습니다.
            # 세팅된 Provider별 설정현황을 social\_app 속성으로 지정해보겠습니다.
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            # Provider 설정이 없을 경우 .social_app을 None으로 설정
            provider.social_app = None
        provider_list.append(provider)

    return auth_login(request, form_class=LoginForm,
            extra_context={
                'provider_list': provider_list,
            })


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

