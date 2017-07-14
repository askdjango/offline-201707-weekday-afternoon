from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'query': query,
    })

