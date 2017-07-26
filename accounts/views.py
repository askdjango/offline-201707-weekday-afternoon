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
    return auth_login(request, form_class=LoginForm)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

