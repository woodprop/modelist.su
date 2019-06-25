from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag
from .forms import TagForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'title': 'Последние записи', 'posts': posts})


class PostDetail(View):
    def get(self, request, slug):
        # post = Post.objects.get(slug__iexact=slug)
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})
# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags': tags})


class TagDetail(View):
    def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact=slug)
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})
# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_form.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_form.html', context={'form': bound_form})
