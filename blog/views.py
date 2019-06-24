from django.shortcuts import render


def index(request):
    return render(request, 'blog/articles_list.html', context={'title': 'Главная', 'articles': ['Статья 1', 'Статья 2',
                                                                                                'Статья 3']})
