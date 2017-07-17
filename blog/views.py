import datetime
from django.shortcuts import render
from django.db.models import Q
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)

    date_list = []
    for i in range(366):
        date_list.append(datetime.datetime(2017, 1, 1) + datetime.timedelta(days=i))

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
        'date_list': date_list,
    })


def post_detail(request, pk): 
    post = Post.objects.get(pk=pk)  # 이 코드는 설명을 위한 코드일 뿐, 비추코드 !!!
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


