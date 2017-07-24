from django.shortcuts import render


def profile(request):
    # request.user
    return render(request, 'accounts/profile.html')

