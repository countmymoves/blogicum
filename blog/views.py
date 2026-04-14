from django.shortcuts import render
from django.http import Http404

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': 'Наш корабль потерпел крушение...',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': 'Проснувшись поутру...',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': 'Всю ночь шёл дождь...',
    },
]

# 🔥 удобно для поиска
posts_dict = {post['id']: post for post in posts}


def index(request):
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    if post_id not in posts_dict:
        raise Http404(f'Пост с id={post_id} не найден')

    post = posts_dict[post_id]
    return render(request, 'detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(request, 'category.html', {'category': category_slug})
