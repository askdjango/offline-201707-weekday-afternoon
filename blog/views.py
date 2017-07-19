import datetime
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post
from .forms import PostModelForm


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


def post_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            # form.cleaned_data  # dict타입
            post = form.save()
            return redirect(post)  # post.get_absolute_url() 주소로의 이동을 시도
            # return redirect('blog:post_detail', post.id)
    else:
    # if request.method == 'GET':
        form = PostModelForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })

# from django.views.generic import CreateView
# post_new = CreateView.as_view(model=Post, form_class=PostModelForm, success_url='/weblog/')
# post_new = CreateView.as_view(model=Post, form_class=PostModelForm)


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            # form.cleaned_data  # dict타입
            post = form.save()
            return redirect(post)  # post.get_absolute_url() 주소로의 이동을 시도
        # return redirect('blog:post_detail', post.id)
    else:
        # if request.method == 'GET':
        form = PostModelForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
    })

