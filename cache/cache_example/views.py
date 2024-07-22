from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Post, Category


# Create your views here.
@cache_page(60)
def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'cache_example/post_list.html', {'posts': posts, 'categories': categories})


def post_list_by_category(request, cat_id):
    category = Category.objects.get(id=cat_id)
    cache_key = f'post_list_{cat_id}'
    posts = cache.get(cache_key)

    if not posts:
        posts = Post.objects.filter(category=category)
        cache.set(cache_key, posts, 60*15)

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'cache_example/post_list_by_category.html', context=context)